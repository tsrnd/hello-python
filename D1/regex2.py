import re


def regex(string):
    """This function returns at least one matching digit."""
    pattern = re.compile(r"\d+")
    result = pattern.match(string)
    if result:
        return result.group()
    return None


# Call our function, passing in our string
print(regex("007 James Bond"))
