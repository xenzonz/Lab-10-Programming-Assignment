print("hello world")

"""
Docstring for Lab10_xenzonz_1
i. LAB 9: Word Count
ii. Sam Cocquyt
iii. An OOP-based program that displays a menu of 4 predefined text files, lets the user choose one, then reads and analyzes that file. 
    The program will count the frequency of every word in the selected file and print an alphabetical report.
    WordAnalyzer class will accept an optional list of "stop words" during initialization.
iv. No starter code
v. 3/15/2026
"""

import string
from pathlib import Path

class WordAnalyzer:
    
    def __init__(self, filepath):
        
        self.__filepath = Path(filepath)
        self.__frequency = {}
    
    def process_file(self) -> bool:
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError
            
            translator = str.maketrans("", "", string.punctuation)

        except FileNotFoundError:
            print(f"file not found: {self.__filepath}")
            return False
    
    def print_report(self):
        return 0
    
def main():
    return 0

if __name__ == "__main__":
    main()
