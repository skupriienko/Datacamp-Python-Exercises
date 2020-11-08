def has_docstring(func):
    """Check to see if the function
        `func` has a docstring.

    Args:
        func (callable): A function.

    Returns:
        bool
    """
    return func.__doc__ is not None


# Call has_docstring() on the as_2D() function
ok = has_docstring(as_2D)

if not ok:
    print("as_2D() doesn't have a docstring!")
else:
    print("as_2D() looks ok")

# Call has_docstring() on the log_product() function
ok = has_docstring(log_product)

if not ok:
    print("log_product() doesn't have a docstring!")
else:
    print("log_product() looks ok")
