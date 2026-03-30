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

            with self.__filepath.open("r", encoding="utf-8") as file:
                for line in file:
                    cleaned_line = line.lower().translate(translator)
                    cleaned_words: list[str] = cleaned_line.split()

                    for word in cleaned_words:
                        if word in self.__frequency:
                            self.__frequency[word] += 1
                        else:
                            self.__frequency[word] = 1

            return True

        except FileNotFoundError:
            print(f"File not found: {self.__filepath}")
            return False
    
    def print_report(self):

        sorted_words = sorted(self.__frequency.keys())

        for word in sorted_words:
            print(f"{word}: {self.__frequency[word]}")
    
def main():

    analyzer = WordAnalyzer("Tarzan.txt")

    if analyzer.process_file():
        analyzer.print_report()


if __name__ == "__main__":
    main()
