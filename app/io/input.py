import pandas as panda
def input_text():
    """
    Prompts the user to input text from the console.

    Examples:
        >>> input_text()
        'Hi'

    Returns:
        str: The text inputted by the user.
     """
    return input("Input text: ")

def read_file_python(file_path):
    """
    Reads the content of a file using Python's built-in methods.

    Args:
        file_path (str): The path to the file to be read.

    Raises:
        FileNotFoundError: If the file does not exist.
        TypeError: If file_path is not a string.

    Examples:
        >>> read_file_python('example.txt')
        'Content of file example.txt'

    Returns:
        str: The content of the file.
    """
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"File {file_path} not found."


def read_file_pandas(file_path):
    """
    Reads a file using the 'pandas' library.

    Args:
        file_path (str): The path to the file to be read.

    Raises:
        FileNotFoundError: If the file does not exist.
        TypeError: If file_path is not a string.

    Examples:
        >>> read_file_pandas('data.csv')
        DataFrame with the content of the file.

    Returns:
        pandas.DataFrame: The content of the file as a DataFrame.
    """
    try:
        return panda.read_csv(file_path)
    except FileNotFoundError:
        return f"File {file_path} not found."