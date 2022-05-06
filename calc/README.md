# CALCULATOR
##Description
Module for simple mathematical calculations.
Two operating modes.
Single operation mode. 
Row mode with multiple operations in an expression.
The modes are switched by the "STR" button.

Functions for one argument have been added to the usual arithmetic operations.
* The inverse function - "1/x"
* The length of the circle by radius - "L circle_r"
* The area of the circle by radius - "S circle_r"
* The volume of the ball by radius - "V ball_r"
* Square root - "2√x"
* Cubic root - "3√x"
* Exponentiation - "^"
* Canceling the last input (only in the mode "STR") - "<<<"
* Reset values - "CE"

##Project composition
#####Functionality - 3 modules:
* **main.py** - main "tkinter" widget assembly module
* **expression.py** - calculation functional module by expression string
* **one_action.py** - calculation functional module for one function
#####Tests - 2 modules:
* **expression_test.py** - tests for module expression.py
* **one_action_test.py** - tests for module one_action.py
#####Run file:
* **main.exe**

##DevelopmentrRequirements
####Python 3.10.0
* unitest
* doctest
* tkinter
* numexpr
* numpy
* math

####Packages(pip_requirements.txt):
* astroid==2.9.3
* isort==5.10.1 
* lazy-object-proxy==1.7.1
* mccabe==0.6.1
* numexpr==2.8.1
* numpy==1.22.3
* packaging==21.3
* platformdirs==2.4.1
* pylint==2.12.2
* pyparsing==3.0.8
* pytz==2021.3
* toml==0.10.2
* typing-extensions==4.0.1
* ufw==0.36
* wrapt==1.13.3

##Code start
Download three main function files(main.py, expression.py, one_action.py ).
And run the main.py through the IDE.
Terminal - command: **python main.py**.
Or download one file: **main.exe** to your desktop and run it.