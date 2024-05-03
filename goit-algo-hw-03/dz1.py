import os
import shutil
from pathlib import Path

source_path = "goit-algo-hw-03/TestPath"
target_path = "dist"

def is_accessible(path):
    return os.access(path, os.R_OK)

def get_file_extension(file_name):
    return os.path.splitext(file_name)[1]


def copy_to_newdir(to_dir:str, source_file:str, name_file:str) -> None:
    #print(to_dir)
    #print(source_file)
    #print(name_file)
    
    if not os.path.exists(to_dir):
        os.makedirs(to_dir)
    shutil.copy(source_file, to_dir + "/" + name_file)
    
def recursive_tree(path: Path, indent: str = "") -> None:
    
    if path.is_dir():
        for child in path.iterdir():
            recursive_tree(child, indent + "    ")
    else:
        if is_accessible(path):
            copy_to_newdir(target_path +"/"+ get_file_extension(path.name), path, path.name)
    

if __name__ == "__main__":
    input_str = input("Введите два аргумента через пробел: ")
    arguments = input_str.split()

    if len(arguments) == 1:
        source_path = arguments[0]
    if len(arguments) == 2:
        target_path = arguments[1]
        
    root = Path(source_path)
    recursive_tree(root)
    
    if len(arguments) == 0:
        print("Не введены аргументы? Я всеравно создал копию!")
   