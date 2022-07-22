"""Local utility module that handles printing error and success messages.

This module exports the following functions:
    print_error - prints and formats an error message.
    print_success - prints and formats a success message.
"""
# authors:
# @markoprodanovic
# 
# last edit:
# Monday, January 12, 2020

from termcolor import cprint
import sys


def print_error(msg):
    """ Print the error message without shutting down the script.

    parameters:
        msg (string): Message to print before continuing execution
    """
    cprint(f"\n{msg}\n", "red")


def print_success(msg):
    """ Print a message indicating success and continuation of script.

    parameters:
        msg (string): Message to print before continuing execution
    """
    cprint(f"\n{msg}\n", "green")

