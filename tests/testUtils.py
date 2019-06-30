import unittest
from utils import verify_types, verify_positive


# Class, used for method decorators testing
class ToBeVerified:
    def __init__(self):
        self.args = None

    @verify_types([int, float], str)
    def setTypes(self, arg1, arg2):
        return None

    @verify_positive
    def setPositive(self, arg1):
        return None


class TestVerifyTypes(unittest.TestCase):
    def setUp(self):
        self.obj = ToBeVerified()

    def test_good_case(self):
        self.assertIsNone(self.obj.setTypes(5, 'fhgkdfg'))
        self.assertIsNone(self.obj.setTypes(5.2, 'jfhghsf'))

    def test_wrong_type_argument1(self):
        with self.assertRaises(TypeError):
            self.obj.setTypes('jhhfg', 'jfhgdf')

    def test_wrong_argument2(self):
        with self.assertRaises(TypeError):
            self.obj.setTypes(5, 4)


class TestVerifyPositive(unittest.TestCase):
    def setUp(self):
        self.obj = ToBeVerified()

    def test_good_case(self):
        self.assertIsNone(self.obj.setPositive(5))

    def test_wrong_value_argument(self):
        with self.assertRaises(ValueError):
            self.obj.setPositive(-2)

    def test_with_not_numeric(self):
        self.assertIsNone(self.obj.setPositive("A"))

    def test_list_of_values(self):
        self.assertIsNone(self.obj.setPositive(['a', 5, 5.6, 'fjhgd', [4, 5]]))


if __name__ == '__main__':
    unittest.main()
