import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"Train script for {ROOT}.")
print("This task type uses a pretrained model. Place weights in models/ (e.g. whisper/base for your-task).")
