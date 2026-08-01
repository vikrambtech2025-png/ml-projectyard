import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from model_registry import find_models  # noqa: E402


class TestApp(unittest.TestCase):
    def test_app_importable(self):
        import app
        self.assertTrue(hasattr(app, "demo"))

    def test_interface_builds(self):
        import app
        self.assertIsNotNone(app.demo)

    def test_model_registry(self):
        models = find_models()
        self.assertIsInstance(models, list)

    def test_config_dirs_exist(self):
        import config
        self.assertTrue(os.path.isdir(config.MODEL_DIR))
        self.assertTrue(os.path.isdir(config.DATA_DIR))


if __name__ == "__main__":
    unittest.main()
