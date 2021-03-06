# About

*Calculator* is a program that allows to perform calculations in prefix and infix notations.

The following assumptions are made:

* The calculator supports the operators {+, -, *, /} which all take exactly two args.

* The input literals are positive integers.

* Operator precedence is not handled.

# Setup instructions

*Calculator* has been built using Python 3.7.  
Please note this installation has been tested on macOS 10.14 and Ubuntu 18.04. 

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

You can create a virtual environment using `virtualenv`. If `virtualenv` is not installed in your machine, install it with the command:

```
pip install virtualenv
```

Then create the virtual environment `calculator` and install all the required packages by running the following command from the root directory of the repository:

```
source setup_virtualenv.sh
```

# Usage example

Prefix and infix operations are defined in two separate classes. The code snippet below provides an example of a prefix operation:

```python
from calculator import PrefixOperation

test_expression = "+ 3 4"

# Create an instance of the prefix class and evaluate the expression
prefix = PrefixOperation(test_expression)
result = prefix.evaluate_expression()
print(result)
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

# Docker
*Calculator* can be containerised using Docker.

Build a Docker image called `calculator` from the provided `Dockerfile` and tag the image with `latest`:
```
docker build -f Dockerfile -t calculator:latest .
```

Run a Docker container from the built `container` image:
```
docker run -p 5000:5000 -d calculator:latest
```
5000:5000 means redirecting traffic from port 5000 on all interfaces in the main network namespace to the container's port 5000 on its external interface.

The app is now available at http://127.0.0.1:5000/.

