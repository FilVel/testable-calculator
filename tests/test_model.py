import unittest
from calculator import Calculator


class TestCalculatorMethods(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_initial_expression_is_empty(self):
        self.assertEqual("", self.calculator.expression)

    def test_digit(self):
        self.calculator.digit(1)
        self.assertEqual("1", self.calculator.expression)

    def test_plus(self):
        self.calculator.plus()
        self.assertEqual("+", self.calculator.expression)

    def test_minus(self):
        self.calculator.minus()
        self.assertEqual("-", self.calculator.expression)
    
    def test_multiply(self):
        self.calculator.multiply()
        self.assertEqual("*", self.calculator.expression)
    
    def test_divide(self):
        self.calculator.divide()
        self.assertEqual("/", self.calculator.expression)
    
    def test_open_parenthesis(self):
        self.calculator.parenthesis(open=True)
        self.assertEqual("(", self.calculator.expression)
    
    def test_closed_parenthesis(self):
        self.calculator.parenthesis(open=False)
        self.assertEqual(")", self.calculator.expression)
    
    def test_square_root(self):
        self.calculator.square_root()
        self.assertEqual("math.sqrt(", self.calculator.expression)

    def test_power_two(self):
        self.calculator.power_two()
        self.assertEqual("**(", self.calculator.expression)


class TestCalculatorUsage(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_expression_insertion(self):
        self.calculator.digit(1)
        self.calculator.plus()
        self.calculator.digit(2)
        self.assertEqual("1+2", self.calculator.expression)

    def test_compute_result(self):
        self.calculator.expression = "1+2"
        self.assertEqual(3, self.calculator.compute_result())

    def test_compute_result_with_invalid_expression(self):
        self.calculator.expression = "1+"
        with self.assertRaises(ValueError) as context:
            self.calculator.compute_result()
        self.assertEqual("Invalid expression: 1+", str(context.exception))

class TestComplexExpressions(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_involving_parenthesis(self):
        # (1+2)*3 == 9
        self.calculator.parenthesis(True)
        self.calculator.digit(1)
        self.calculator.plus()
        self.calculator.digit(2)
        self.calculator.parenthesis(False)
        self.calculator.multiply()
        self.calculator.digit(3)
        self.assertEqual(9, self.calculator.compute_result())

    def test_square_rot(self):
        # sqrt(2+2)*3 == 6
        self.calculator.square_root()
        self.calculator.digit(2)
        self.calculator.plus()
        self.calculator.digit(2)
        self.calculator.parenthesis(False)
        self.calculator.multiply()
        self.calculator.digit(3)
        self.assertEqual("math.sqrt(2+2)*3", self.calculator.expression)
        self.assertEqual(6.0, self.calculator.compute_result())
        self.assertEqual('6.0', self.calculator.expression)
    
    def test_power_two(self):
        # (1+3-2)**3 == 8
        self.calculator.parenthesis(True)
        self.calculator.digit(1)
        self.calculator.plus()
        self.calculator.digit(3)
        self.calculator.minus()
        self.calculator.digit(2)
        self.calculator.parenthesis(False)
        self.calculator.power_two()
        self.calculator.digit(3)
        self.calculator.parenthesis(False)
        self.assertEqual("(1+3-2)**(3)", self.calculator.expression)
        self.assertEqual(8.0, self.calculator.compute_result())
        self.assertEqual('8', self.calculator.expression)
        
