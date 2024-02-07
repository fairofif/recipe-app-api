from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    def test_add_number_success(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_add_number_failed(self):
        res = calc.add(5, -5)
        self.assertNotEqual(res, 1)
