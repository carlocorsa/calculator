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

If you have `conda` installed and want to create a `conda` environment, create the environment `calculator` and install all the required packages by running the command:

```
source setup_conda_env.sh
```

## Using virtualenv and pip

If `virtualenv` is not installed in your machine, install it with the command:

```
pip install virtualenv
```

Then create the virtual environment `calculator` and install all the required packages by running the following command from the root directory of the repository:

```
source setup_virtualenv.sh
```

# Testing
If you have created the environment using either `setup_conda_env.sh` or `setup_virtualenv.sh`, the required packages for testing have already been installed in your environment. Otherwise, install them by running the following command:

```
pip install -r tests/requirements.txt
``` 

To test the program, run the following commands:

```
python -m unittest -v tests/test_prefix_calculator.py
```
and
```
python -m unittest -v tests/test_infix_calculator.py
```

# Web application
*Calculator* can be used as a web application.

To access the application locally, run the following command:

```
python app.py
```

and head over http://127.0.0.1:5000/.
