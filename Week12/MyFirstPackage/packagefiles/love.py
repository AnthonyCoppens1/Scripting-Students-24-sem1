def calculate(name1, name2):
    """calculates the love percentage between 2 given names
    Parameters:
        string --> name1
        string --> name2
    Return:
        The percentage    
    """
    firstlength = len(name1)
    secondlength = len(name2)

    difference = firstlength - secondlength

    if difference <= 2:
        return "90% match"
    elif difference <= 4:
        return "80% match"
    elif difference <= 6:
        return "70% match"
    elif difference <= 8:
        return "60% match"
    else:
        return "no match"


from difflib import SequenceMatcher
def calculate2(name1, name2):
    """calculates the love percentage between 2 given names with a similarity check
    Parameters:
        string --> name1
        string --> name2
    Return:
        The percentage    
    """
    calculation = round(SequenceMatcher(None, name1, name2).ratio()*100,0)
    return str(calculation) + "% match"