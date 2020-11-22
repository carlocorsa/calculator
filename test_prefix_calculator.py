import unittest
from calculator import PrefixOperation


def print_operations(prefix, infix):
    """Print prefix and infix operations.

    Parameters
    ----------
    prefix: str
        Prefix operation

    infix: str
        Infix operation
    """

    print("\nThe prefix operation '{}' is equivalent to the infix operation '{}'.".format(prefix, infix))


class TestPrefix(unittest.TestCase):

    def test_single_digit(self):
        """Test that a single digit is evaluated correctly."""

        prefix = "3"
        infix = "3"
        self.assertEqual(eval(infix), PrefixOperation(prefix).evaluate_expression())
        print_operations(prefix, infix)

    def test_single_operation(self):
        """Test that single operations are evaluated correctly."""

        prefix = "+ 1 2"
        infix = "1 + 2"
        self.assertEqual(eval(infix), PrefixOperation(prefix).evaluate_expression())
        print_operations(prefix, infix)

        prefix = "- 0 3"
        infix = "0 - 3"
        self.assertEqual(eval(infix), PrefixOperation(prefix).evaluate_expression())
        print_operations(prefix, infix)

        prefix = "/ 3 2"
        infix = "3 / 2"
        self.assertEqual(eval(infix), PrefixOperation(prefix).evaluate_expression())
        print_operations(prefix, infix)

    def test_two_operations(self):
        """Test that two consecutive operations are evaluated correctly."""

        prefix = "+ 1 * 2 3"
        infix = "1 + 2 * 3"
        self.assertEqual(eval(infix), PrefixOperation(prefix).evaluate_expression())
        print_operations(prefix, infix)

        prefix = "+ * 1 2 3"
        infix = "1 * 2 + 3"
        self.assertEqual(eval(infix), PrefixOperation(prefix).evaluate_expression())
        print_operations(prefix, infix)

    def test_multiple_operations(self):
        """Test that multiple prefix operations without spaces after operators are evaluated correctly."""

        prefix = "-/10 +1 1 *1 2"
        infix = "10 / (1 + 1) - (1 * 2)"
        self.assertEqual(eval(infix), PrefixOperation(prefix).evaluate_expression())
        print_operations(prefix, infix)


if __name__ == '__main__':
    unittest.main()
