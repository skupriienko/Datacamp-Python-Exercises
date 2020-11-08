import re

# Complete the function's docstring
def tokenize(text, regex=r'[a-zA-z]+'):
    """Split text into tokens using a regular expression

    :param text: text to be tokenized
    :param regex: regular expression used to match tokens using re.findall
    :return: a list of resulting tokens

    >>> tokenize('the rain in spain')
    ['the', 'rain', 'in', 'spain']
    """
    return re.findall(regex, text, flags=re.IGNORECASE)

tk = tokenize('the rain in spain')
print(tk)
# Print the docstring
help(tokenize)
