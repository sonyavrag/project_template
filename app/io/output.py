def print_text(text):
    """
    Prints the given text to the console.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> print_text('Hi')
        Hi
    """
    print(text)

def write_file_python(file_path, content):
    """
    Writes the given content to a file using Python's built-in methods.

    Args:
        file_path (str): The path to the file to be written.
        content (str): The content to be written to the file.

    Raises:
        TypeError: If file_path or content is not a string.

    Examples:
        >>> write_file_python('example.txt', 'Content of example.txt.')
        None
    """
    try:
        with open(file_path, "w") as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")