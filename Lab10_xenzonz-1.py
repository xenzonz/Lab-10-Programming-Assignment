
"""
Docstring for Lab10_xenzonz_1
i. LAB 10: Word Count
ii. Sam Cocquyt
iii. An OOP-based program that displays a menu of 4 predefined text files, lets the user choose one, then reads and analyzes that file. 
    The program will count the frequency of every word in the selected file and print an alphabetical report.
    WordAnalyzer class will accept an optional list of "stop words" during initialization.
iv. No starter code
v. 3/29/2026
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
            
            translator = str.maketrans("", "", string.punctuation + "“”‘’")

            with self.__filepath.open("r", encoding="utf-8-sig") as file:
                for line in file:
                    cleaned_line = line.lower().translate(translator)
                    cleaned_words: list[str] = cleaned_line.split()

                    for word in cleaned_words:
                        if not word.isalpha(): #remove numbers
                            continue
                        if word.startswith("www"): #remove wwwgutenbergorg etc.
                            continue

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
            print(f"{word:<25}:: {self.__frequency[word]}")


def file_menu():

    base_path = Path(__file__).parent
    file_options: dict[str, Path] = {
        "1": base_path / "monte_cristo.txt",
        "2": base_path / "princess_mars.txt",
        "3": base_path / "Tarzan.txt",
        "4": base_path / "treasure_island.txt",
    }

    return file_options

def display_name(filepath: Path) -> str:
    return filepath.stem.replace("_", " ").title()
    
def main():
    files = file_menu()
    exit_key = str(len(files) + 1) #"5" when there are 4 files, etc.

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")

        for key, filepath in files.items():
            print(f"  {key}. {display_name(filepath)}")
        print(f"  {exit_key}. Exit\n")

        choice = input(f"Enter your choice (1-{exit_key}): ").strip()

        if choice == exit_key:
            print("\nGoodbye!")
            break

        if choice not in files:
            print(f"\nInvalid choice. Please select from 1-{exit_key}.")
            input("\nPress Enter to return to the menu... ")
            continue

        filepath = files[choice]
        print(f"\nProcessing '{filepath.name}'...\n")

        analyzer = WordAnalyzer(filepath)
        if analyzer.process_file():
            analyzer.print_report()

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
