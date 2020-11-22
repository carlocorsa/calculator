import operator


# Define dictionary with operators
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


class PrefixOperation:

    def __init__(self, expression):
        self.expression = str(expression)
        self.rev_elems = None
        self.parse_expression()

    def parse_expression(self):
        """Initialise object attribute 'rev_elems' by taking
        all elements in the expression in reverse order."""

        # Add a space before and after each operator to make sure elements are split correctly
        expression = "".join([" {} ".format(el) if not el.isdigit() else el for el in self.expression])

        # Split and reverse elements
        self.rev_elems = expression.split()[::-1]

    def evaluate_expression(self):
        """Compute the prefix operations by evaluating the expression in reverse order."""

        # Create an empty list to store operands
        operands = []

        # Loop through the reversed expression elements
        for element in self.rev_elems:

            # Store element in the operands list if it is a digit
            if element.isdigit():
                operands.append(float(element))

            else:
                # Get operands for the operation and remove them from the list
                try:
                    num1 = operands.pop(-1)
                    num2 = operands.pop(-1)
                except IndexError:
                    return

                # Compute the operation and append the result to the operands list
                try:
                    operands.append(ops[element](num1, num2))
                except KeyError:
                    return

        if len(operands) == 1:
            return operands.pop()
        else:
            return


class InfixOperation:

    def __init__(self, expression):
        self.expression = str(expression)
        self.elements = None
        self.parse_expression()

    def parse_expression(self):
        """Initialise object attribute 'elements'."""

        # Add a space before and after each operator to make sure elements are split correctly
        expression = "".join([" {} ".format(el) if not el.isdigit() else el for el in self.expression])

        # Split and reverse elements
        self.elements = expression.split()

    def evaluate_expression(self):
        """Compute the infix operations."""

        # Create an empty list to store operands and operators
        terms = []

        # Create a copy of the elements
        elements = self.elements[:]

        # Loop through all elements in the expression
        while elements:

            # Remove first element from list
            el = elements.pop(0)

            # Store operands and digits
            if el.isdigit() or el in ops:
                terms.append(el)

            # When reaching a close parenthesis compute one operation
            elif el == ")":
                try:
                    num2 = float(terms.pop())
                    op = terms.pop()
                    num1 = float(terms.pop())
                except (IndexError, ValueError):
                    return

                # Compute the operation and append the result to the terms list
                try:
                    terms.append(ops[op](num1, num2))
                except KeyError:
                    return

        # Perform any outstanding operation
        while len(terms) > 1:
            try:
                num2 = float(terms.pop())
                op = terms.pop()
                num1 = float(terms.pop())
            except (IndexError, ValueError):
                return

            try:
                terms.append(ops[op](num1, num2))
            except KeyError:
                return

        return terms.pop()
