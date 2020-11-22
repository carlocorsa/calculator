import unittest
from parameterized import parameterized
from calculator import InfixOperation


class TestInfix(unittest.TestCase):

    @parameterized.expand([
        ["( 1 + 2 )"],  # single operation
        ["( 1 + ( 2 * 3 ) )"],  # double operation
        ["( ( 1 * 2 ) + 3 )"],  # double operation
        ["(((1+1)/10)-(1*2))"]  # multiple operation without spaces
    ])
    def test_operation(self, expression):
        """Test a valid operation.

        Parameters
        ----------
        expression: str
            Evaluation to be evaluated.
        """

        self.assertEqual(eval(expression), InfixOperation(expression).evaluate_expression())

    def test_invalid(self):
        """Test an invalid expression."""

        expression = "1 + 3 * 5 + 7"  # It needs parentheses because operator precedence is not handled.

        self.assertNotEqual(eval(expression), InfixOperation(expression).evaluate_expression())


if __name__ == '__main__':
    unittest.main()
