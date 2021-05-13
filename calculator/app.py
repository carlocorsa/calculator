from flask import Flask, request, render_template, url_for
from calculator import PrefixOperation, InfixOperation

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/prefix", methods=["GET", "POST"])
def evaluate_prefix():

    # Display the prefix calculator page
    if request.method == 'GET':
        return render_template('calculator.html', title='Prefix')

    # Evaluate an expression
    elif request.method == 'POST':

        expression = request.form.get('expression')
        result = PrefixOperation(expression).evaluate_expression()
        if result is None:
            result = "Invalid expression"
        else:
            result = str(result)

        return render_template('calculator.html', title='Prefix', result=result)


@app.route('/infix', methods=['GET', 'POST'])
def evaluate_infix():

    # Display the infix calculator page
    if request.method == 'GET':
        return render_template('calculator.html', title='Infix')

    # Evaluate an expression
    elif request.method == 'POST':
        expression = request.form.get('expression')
        result = InfixOperation(expression).evaluate_expression()
        if result is None:
            result = "Invalid expression"
        else:
            result = str(result)

        return render_template('calculator.html', title='Infix', result=result)


# run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

