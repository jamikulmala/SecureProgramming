import re

# Program that reads a file and filters all characters except letter’s, numbers, commas and hyphen.

def filter_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            filtered_content = re.sub(r'[^a-zA-Z0-9, -]', '', file_content)
            print(filtered_content)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

filter_file('t3.txt')