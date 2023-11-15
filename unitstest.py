import unittest
from app import app
from app.validate import validate, validate_addition


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        pass

    def test_app(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_validate_text_pass(self):
        result = validate('abcde12345')
        self.assertTrue(result[1])
        self.assertEqual(result[0], 'abcde12345')

    def test_validate_text_fail(self):
        result = validate(r"abcd&><'\"efgh")
        self.assertFalse(result[1])
        self.assertNotEqual(result[0], r"abcd&><'\"efgh")

    def test_validate_calculator_pass(self):
        result = validate_addition("123", "321")
        self.assertTrue(result[1])
        self.assertEqual(result[0], "444")

    def test_validate_calculator_fail1(self):
        result = validate_addition(r"abcd&><'\"efgh", "321")
        self.assertFalse(result[1])
        self.assertEqual(result[0], "0")

    def test_validate_calculator_fail2(self):
        result = validate_addition("123", r"abcd&><'\"efgh")
        self.assertFalse(result[1])
        self.assertEqual(result[0], "0")

    def test_validate_calculator_fail3(self):
        result = validate_addition(r"abcd&><'\"efgh", r"abcd&><'\"efgh")
        self.assertFalse(result[1])
        self.assertEqual(result[0], "0")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()