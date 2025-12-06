"""
a script module
"""

from steps import hello_pre_commit


def using_hello():
    """
    A method that calls hello from the hello_pre_commit script
    """
    hello_pre_commit.hello()


using_hello()
