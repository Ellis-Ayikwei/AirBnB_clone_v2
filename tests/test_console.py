import unittest
from console import HBNBCommand

class TestCreateCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console

    def test_create_with_string_parameter(self):
        self.console.do_create("Base name=\"My_little_house\"")
        self.assertIn("My little house", self.console.stdout.getvalue())

    def test_create_with_float_parameter(self):
        self.console.do_create("Base value=3.14")
        self.assertIn("3.14", self.console.stdout.getvalue())

    def test_create_with_integer_parameter(self):
        self.console.do_create("Base number=42")
        self.assertIn("42", self.console.stdout.getvalue())

    def test_create_with_invalid_parameter(self):
        self.console.do_create("Base invalid_param=invalid_value")
        self.assertIn("** Unknown syntax: invalid_param=invalid_value **", self.console.stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
