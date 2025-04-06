from app.io.input import input_text, read_file_python, read_file_pandas
from app.io.output import print_text, write_file_python


def main():
    user_input = input_text()
    file_content_python = read_file_python("data/file.txt")
    file_content_pandas = read_file_pandas("data/file.csv")

    print_text(user_input)
    print_text(file_content_python)
    print_text(file_content_pandas)

    write_file_python("output/user_input.txt", user_input)
    write_file_python("output/python_file_content.txt", file_content_python)
    write_file_python("output/pandas_file_content.txt", str(file_content_pandas))

if __name__ == '__main__':
    main()
