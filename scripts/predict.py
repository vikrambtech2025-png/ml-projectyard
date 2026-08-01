import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "src"))

from model_registry import find_models  # noqa: E402

models = find_models()
if not models:
    print("STATUS: NO_MODEL")
    sys.exit(1)
for m in models:
    print(f"MODEL: {m}")
print("STATUS: OK")
