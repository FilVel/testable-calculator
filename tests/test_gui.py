import os ; os.environ["KIVY_NO_ARGS"] = "1" # hack for making tests loadable in VS Code
import unittest
from calculator.ui.gui import CalculatorApp


class CalculatorGUITestCase(unittest.TestCase):
    def setUp(self):
        self.app = CalculatorApp()
        self.app._run_prepare()

    def press_button(self, button_text):
        button = self.app.find_button_by(button_text)
        if button is None:
            raise AssertionError(f"Missing button: {button_text}")
        button.trigger_action()

    def assert_display(self, value):
        self.assertEqual(self.app.display.text, value)   

    def tearDown(self):
        self.app.stop()

EXPECTED_BUTTON_NAMES = { '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '.', '0', '=', '+', '(', ')', '^', '√', 'C' }

class TestAllButtonsExist(CalculatorGUITestCase):
    def test_all_buttons_exist(self):
        for button in EXPECTED_BUTTON_NAMES:
            with self.subTest(button_name=button):
                self.press_button(button)

class TestExpressions(CalculatorGUITestCase):
    def compose_expression(self, exp: str):
        for char in exp:
            self.press_button(char)
        self.assert_display(exp)
        
    def test_integer_expression(self):
        self.compose_expression("1+2")
        self.press_button("=")
        self.assert_display("3")

    def test_float_expression(self):
        self.compose_expression("1.2+2")
        self.press_button("=")
        self.assert_display("3.2")

    def test_complex_equation(self):
        # test that (1+2)*3 == 9 
        self.press_button("(")
        self.assert_display("(")
        self.press_button("1")
        self.assert_display("(1")
        self.press_button("+")
        self.assert_display("(1+")
        self.press_button("2")
        self.assert_display("(1+2")
        self.press_button(")")
        self.assert_display("(1+2)")
        self.press_button("*")
        self.assert_display("(1+2)*")
        self.press_button("3")
        self.assert_display("(1+2)*3")
        self.press_button("=")
        self.assert_display("9")

    def test_sqrt_expression(self):
        # test that sqrt(5-1) - 1 == 1
        self.press_button("√")
        self.assert_display("√(")
        self.press_button("5")
        self.assert_display("√(5")
        self.press_button("-")
        self.press_button("1")
        self.press_button(")")
        self.assert_display("√(5-1)")
        self.press_button("-")
        self.assert_display("√(5-1)-")
        self.press_button("1")
        self.assert_display("√(5-1)-1")
        self.press_button("=")
        self.assert_display("1.0")

    def test_power_expression(self):
        # test that (4 / 2) ** (5 - 1) == 16
        self.compose_expression("(4/2)")
        self.press_button("^") # ^ is the symbol for power that we wanna have in our GUI
        self.assert_display("(4/2)^(")
        self.press_button("5")
        self.press_button("-")
        self.press_button("1")
        self.press_button(")")
        self.assert_display("(4/2)^(5-1)")
        self.press_button("=")
        self.assert_display("16.0")

    def test_clear_button(self):
        # test that the button clear works as intended
        self.compose_expression("(4)")
        self.press_button("C")
        self.assert_display("0")
        self.press_button("1")
        self.assert_display("1")

    def test_errors(self):
        # test that 0/0 throws an error
        self.compose_expression("0/0")
        self.press_button("=")
        self.assert_display("Error")
        self.press_button("1")
        self.press_button("+")
        self.press_button("=")
        self.assert_display("Error")