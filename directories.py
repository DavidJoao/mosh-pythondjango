from pathlib import Path

#Absolute path
#Starts from the root of the hard disk
#Relative path
#Starts from current directory
p = Path('ecommerce')
for file in p.glob('*.py'):
    print(file)