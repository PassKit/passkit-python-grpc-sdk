"""Smoke tests for every module shipped in the SDK."""

import importlib
import inspect
import pkgutil
import unittest

import passkit


class PackageImportTests(unittest.TestCase):
    def test_version_matches_release(self):
        self.assertEqual(passkit.__version__, "1.1.162")

    def test_every_module_imports(self):
        modules = [
            module.name
            for module in pkgutil.walk_packages(passkit.__path__, "passkit.")
        ]

        self.assertGreater(len(modules), 100)
        for module in modules:
            with self.subTest(module=module):
                importlib.import_module(module)

    def test_legacy_module_getters(self):
        package_names = [
            module.name
            for module in pkgutil.walk_packages(passkit.__path__, "passkit.")
            if module.ispkg
        ]

        for package_name in package_names:
            package = importlib.import_module(package_name)
            getters = [
                function
                for name, function in inspect.getmembers(package, inspect.isfunction)
                if name.startswith("get_")
            ]
            for getter in getters:
                with self.subTest(package=package_name, getter=getter.__name__):
                    self.assertIsNotNone(getter())


if __name__ == "__main__":
    unittest.main()
