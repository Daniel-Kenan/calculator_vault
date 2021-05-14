from sys import path
from tkinter import filedialog as fd
import os , getpass
EXECUTION_PATH  =os.path.dirname(os.path.abspath(__file__))
ORIGIN_PATH = EXECUTION_PATH +"\\.data\\"

def retrieve(): 
    os.system('attrib -s -h .data && cd .data && attrib -s -h *')
    hidden_files = fd.askopenfilenames(initialdir = '.data' , title= "SELECT FILES TO RETRIEVE")
    dump_dir = fd.askdirectory(initialdir = f'c:/users/{getpass.getuser()}/documents' , title = "SELECT A FOLDER TO RECOVER TO") + "/"
    for data in hidden_files:
        path_reversed = data[::-1]
        path = path_reversed[:path_reversed.index('/')]
        title = path[::-1] 
        os.system(f'cd "{ORIGIN_PATH}" && move "{title}" "{dump_dir}"')
    os.system('cd .data && attrib +s +h * && cd .. && attrib +s +h .data')


def classify():
    files_to_hide = fd.askopenfilenames()
    
    for data in files_to_hide:
        path_reversed = data[::-1]
        path = path_reversed[:path_reversed.index('/')]
        absolute_path = path_reversed[path_reversed.index('/'):]
        title = path[::-1] 
        absolute_path = absolute_path[::-1]
        os.system(f'cd "{absolute_path}" && move "{title}" "{ORIGIN_PATH}" && cd "{ORIGIN_PATH}" && attrib +s +h *')
        print(absolute_path)
        print(title)
        print(ORIGIN_PATH)
