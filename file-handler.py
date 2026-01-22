import os

def create_file(filename):
    try:
        with open(filename, 'x'):
            print(f"File '{filename}' created successfully.")
    except FileExistsError:
        print(f"File '{filename}' already exists.")
    except OSError as error:
        print(f"Error creating file: {error}")


def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print("Content written successfully.")
    except OSError as error:
        print(f"Error writing to file: {error}")


def append_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content)
            print("Content appended successfully.")
    except OSError as error:
        print(f"Error appending to file: {error}")


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print("\n--- File Content ---")
            print(data)
    except FileNotFoundError:
        print("File not found.")
    except OSError as error:
        print(f"Error reading file: {error}")


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print("File does not exist.")
    except OSError as error:
        print(f"Error deleting file: {error}")


if __name__ == "__main__":
    file_name = "example.txt"

    create_file(file_name)
    write_to_file(file_name, "Hello, this is a file handler project.\n")
    append_to_file(file_name, "Appending more content.\n")
    read_file(file_name)
    delete_file(file_name)
