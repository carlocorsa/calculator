import unittest
from calculator import InfixOperation


class TestInfix(unittest.TestCase):

    def test_single_operation(self):
        """Test that a single operation is evaluated correctly."""

        expression = "( 1 + 2 )"
        self.assertEqual(eval(expression), InfixOperation(expression).evaluate_expression())
        print("\n{} = {}.".format(expression, eval(expression)))

    def test_two_operations(self):
        """Test that two consecutive operations are evaluated correctly."""

        expression = "( 1 + ( 2 * 3 ) )"
        self.assertEqual(eval(expression), InfixOperation(expression).evaluate_expression())
        print("\n{} = {}.".format(expression, eval(expression)))

        expression = "( ( 1 * 2 ) + 3 )"
        self.assertEqual(eval(expression), InfixOperation(expression).evaluate_expression())
        print("\n{} = {}.".format(expression, eval(expression)))

    def test_multiple_operations(self):
        """Test that multiple infix operations without spaces are evaluated correctly."""

        expression = "(((1+1)/10)-(1*2))"
        self.assertEqual(eval(expression), InfixOperation(expression).evaluate_expression())
        print("\n{} = {}.".format(expression, eval(expression)))


if __name__ == '__main__':
    unittest.main()
