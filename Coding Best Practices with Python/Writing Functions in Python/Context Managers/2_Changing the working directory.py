def in_dir(directory):
        """Change current working directory to `directory`,
    allow the user to run some code, and change back.

    Args:
        directory (str): The path to a directory to work in.
    """
    current_dir = os.getcwd()
    os.chdir(directory)

    # Add code that lets you handle errors
    try:
        yield directory
    # Ensure the directory is reset,
    # whether there was an error or not
    finally:
        os.chdir(current_dir)
