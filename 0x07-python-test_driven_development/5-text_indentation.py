#!/usr/bin/python3
"""text_indentation moduel"""

def text_indentation(text):
    """text_indentation is a function that prints a text
    with 2 new lines after each of these characters: ., ? and :

    Args:
        text: the argument

    Raises:
        TypeError: if the text not a string

    Return:
        nothing
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for sep in ".?:":
        text = (sep + "\n\n").join(
                [line.strip(" ") for line in text.split(sep)])

    print(text, end="")
