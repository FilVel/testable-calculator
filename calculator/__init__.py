import math 

Number = int | float


class Calculator:

    def __init__(self):
        self.expression = ""

    def _ensure_is_digit(self, value: int | str):
        if isinstance(value, str):
            value = int(value)
        if value not in range(10):
            raise ValueError(f"Value must a digit in [0, 9]:  {value}")
        return value

    def _append(self, value):
        self.expression += str(value)
    
    def digit(self, value: int | str):
        value = self._ensure_is_digit(value)
        self._append(value)
    
    def plus(self):
        self._append("+")

    def minus(self):
        self._append("-")
    
    def multiply(self):
        self._append("*")
    
    def divide(self):
        self._append("/")

    def dot(self):
        self._append(".")

    def clear(self):
        self.expression = ""
    
    def parenthesis(self, open: bool):
        if open:
            self._append("(")
        else:
            self._append(")")
    
    def square_root(self):
        self._append("math.sqrt(")
    
    def power_two(self):
        self._append("**(")
    
    def compute_result(self) -> Number:
        try:
            result = eval(self.expression)
            if isinstance(result, int) or isinstance(result, float):
                self.expression = str(result)
                return result
            else:
                raise ValueError("Result is not a number: " + str(result))
        except Exception as e:
            expression = self.expression
            self.expression = ""
            raise ValueError("Invalid expression: " + expression) from e
