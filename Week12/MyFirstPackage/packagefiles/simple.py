#simple functions

def helloworld():
    """ a function that prints Hello world!
    Parameters:
        none
    Return:
        none
    """
    print("Hello world!")

def helloname(myname):
    """ a function that prints Hello, followed by a given name
    Parameters:
        string --> myname
    Return:
        none
    """
    print("hello, ", myname)

def sum(x,y):
    """ function that returns the sum of 2 parameters
    Parameters:
        int --> x
        int --> y
    Return:
        int: sum of x and y
    """
    return x+y

def average(x, y):
    """function that returns the average of 2 parameters
    Parameters:
        float --> x
        float --> y
    Return:
        float: average of x and y
    """
    return (x + y)/2

def power(x, y):
    """function that calulates the power y of x
    Parameters:
        int --> x
        int --> y
    Return:
        int: x to the power of y
    """
    return x ** y

