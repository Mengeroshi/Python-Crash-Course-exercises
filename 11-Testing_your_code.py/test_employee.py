import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.xavi = Employee("xavi", "saviñon", 5_000)

    def test_salary_def(self):
        self.xavi.give_rise()
        self.assertEqual(self.xavi.anual_salary, 10_000)
    
    def test_salary(self):
        raised_1 = self.my_salary.give_rise(3_000)
        self.assertEqual(self.xavi.anual_salary,8_000)

    if __name__ == "__main__":
        unittest.main()