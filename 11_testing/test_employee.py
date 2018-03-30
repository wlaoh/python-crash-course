import unittest
import employee

class TestEmployeeClass(unittest.TestCase):
    def setUp(self):
        self.test_employee = employee.Employee('Winston', 'Laoh', '100')
    def test_give_default_raise(self):
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.annual_salary, 5100)
    def test_give_custom_raise(self):
        self.test_employee.give_raise(100)
        self.assertEqual(self.test_employee.annual_salary, 200)