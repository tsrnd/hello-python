def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        fullname = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
