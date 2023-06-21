import os


def parse_file_path(file_path):
    path, file = os.path.split(file_path)
    name, extension = os.path.splitext(file)
    return path, name, extension


path, name, extension = parse_file_path('/Users/UserName/Desktop/example.py')
print(f'Path: {path}')
print(f'Name: {name}')
print(f'Extension: {extension}')
