import glob
import os

from config import MODEL_DIR, PROJECT_ROOT

PRIORITY_EXTS = (".joblib", ".pkl", ".pickle", ".onnx", ".h5", ".hdf5", ".pt", ".pth")
SEARCH_DIRS = ("models", "Model", "model", "Models", "saved_model", "output")

_SKIP_PART = ("checkpoint", "weights", "baseline")


def _scan():
    found = []
    seen = set()
    for d in SEARCH_DIRS:
        base = os.path.join(PROJECT_ROOT, d)
        if not os.path.isdir(base):
            continue
        for ext in PRIORITY_EXTS:
            for path in sorted(glob.glob(os.path.join(base, "**", f"*{ext}"), recursive=True)):
                if path in seen:
                    continue
                seen.add(path)
                found.append(path)
    return found


def find_models():
    found = _scan()
    ranked = []
    for p in found:
        name = os.path.basename(p).lower()
        if any(s in name for s in _SKIP_PART):
            continue
        rank = 0
        if name.startswith("model"):
            rank -= 10
        if "exported" in name:
            rank -= 5
        if name.startswith("best"):
            rank -= 3
        ranked.append((p, rank))
    ranked.sort(key=lambda x: x[1])
    return [p for p, _ in ranked]


def first_model():
    models = find_models()
    return models[0] if models else None


def load_model():
    path = first_model()
    if path is None:
        return None
    if path.endswith((".joblib", ".pkl", ".pickle")):
        import joblib
        return joblib.load(path)
    if path.endswith((".h5", ".hdf5")):
        from tensorflow import keras
        return keras.models.load_model(path)
    if path.endswith((".pt", ".pth")):
        import torch
        return torch.load(path, map_location="cpu")
    if path.endswith(".onnx"):
        import onnxruntime as ort
        return ort.InferenceSession(path)
    return None
