import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
MODEL_DIR = os.path.join(PROJECT_ROOT, "models")
SCRIPT_DIR = os.path.join(PROJECT_ROOT, "scripts")
SRC_DIR = os.path.join(PROJECT_ROOT, "src")

for _d in (DATA_DIR, MODEL_DIR):
    os.makedirs(_d, exist_ok=True)
