def setup_module(module):
    print(f"Setting up module {module.__name__}")


def teardown_module(module):
    print(f"Tearing down module {module.__name__}")


def test_a_function():
    print("RUNNING TEST FUNCTION")


class BaseTest:
    def setup_class(cls):
        print(f"Setting up class {cls.__name__}")

    def teardown_class(cls):
        print(f"Tearing down class {cls.__name__}")

    def setup_method(self, method):
        print(f"Setting up method {method.__name__}")

    def teardown_method(self, method):
        print(f"Tearing down method {method.__name__}")


class TestClass1(BaseTest):
    def test_method_1(self):
        print("RUNNING METHOD 1-1")

    def test_method_2(self):
        print("RUNNING METHOD 1-2")


class TestClass2(BaseTest):
    def test_method_1(self):
        print("RUNNING METHOD 2-1")

    def test_method_2(self):
        print("RUNNING METHOD 2-2")
