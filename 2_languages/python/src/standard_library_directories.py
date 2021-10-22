from pathlib import Path

'''
    params : abolute or relative path
'''
path  = Path()
print(path.exists())
print()

path = Path('python')
print(path.exists())
print()

path = Path('path_creation_test')
print(path.exists())
print()

print('creating path_creation_test directory')
path.mkdir()
print(path.exists())
print()

print('removing path_creation_test directory')
path.rmdir()
print(path.exists())
print()

path = Path('.')
print('print all files and directories in directory')

files_and_directories = path.glob('*') # all files and directories
for item in files_and_directories:
    print(item)
print()


files = path.glob('*.*') # all files 
for item in files:
    print(item)
print()

print('print all python files directory')
python_files = path.glob('*.py') # specific file extension (.py in example)
for python_file in python_files:
    print(python_file)
print()