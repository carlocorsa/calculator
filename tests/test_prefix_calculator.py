import unittest
from parameterized import parameterized
from calculator import PrefixOperation


class TestPrefix(unittest.TestCase):

    @parameterized.expand([
        ["3", "3"],  # single digit
        ["+ 1 2", "1 + 2"],  # single operation
        ["- 0 3", "0 - 3"],  # single operation
        ["/ 3 2", "3 / 2"],  # single operation
        ["+ 1 * 2 3", "1 + 2 * 3"],  # double operation
        ["+ * 1 2 3", "1 * 2 + 3"],  # double operation
        ["-/10 +1 1 *1 2", "10 / (1 + 1) - (1 * 2)"]  # multiple operation without spaces
    ])
    def test_operation(self, prefix_expr, infix_expr):
        """Test a valid operation.

        Parameters
        ----------
        prefix_expr: str
            Prefix expression to be evaluated against infix_expr.

        infix_expr: str
            Infix expression.
        """

        self.assertEqual(eval(infix_expr), PrefixOperation(prefix_expr).evaluate_expression())

    def test_invalid(self):
        """Test an invalid expression."""

        expression = "- 1 + 3"  # Invalid syntax

        self.assertNotEqual(eval(expression), PrefixOperation(expression).evaluate_expression())


if __name__ == '__main__':
    unittest.main()
