# About

*Calculator* is a program that allows to perform calculations in prefix and infix notations.

The following assumptions are made:

* The calculator supports the operators {+, -, *, /} which all take exactly two args.

* The input literals are positive integers.

* Operator precedence is not handled.

# Setup instructions

*Calculator* has been built using Python 3.7.

After cloning the repository:

```
git clone https://github.com/carlocorsa/calculator.git
```

create a python environment with the required packages.

## Using conda

Create the environment `calculator` and install all the required packages by running the command:

```
bash install_conda_env.sh
```

## Using pip

Install the required packages using the `requirements.txt` file:

```
pip install -r requirements.txt
```

# Testing
To test the program, run the following commands:
```
python -m unittest -v test_prefix_calculator.py
```
and
```
python -m unittest -v test_infix_calculator.py
```

# Web application
*Calculator* can be used as a web application.

To access the application locally, run the following command:
```
python app.py
```
and head over http://127.0.0.1:5000/.