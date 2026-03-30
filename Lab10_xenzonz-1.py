
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
    """
    Analyze a text file and count the frequency of alphabetic words.
    """
    def __init__(self, filepath: str | Path) -> None:
        """
        Initialize the analyzer with the path to a text file.

        Args:
            filepath: The path to the file that will be analyzed.
        """
        self.__filepath: Path = Path(filepath)
        self.__frequency: dict[str, int] = {}
    
    def process_file(self) -> bool:
        """
        Read the file and build a frequency dictionary of valid words.

        The text is converted to lowercase, punctuation is removed, and
        only alphabetic words are counted. Words beginning with 'www'
        are skipped.

        Returns:
            True if the file was processed successfully, otherwise False.
        """
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError
            
            translator: dict[int, None] = str.maketrans("", "", string.punctuation + "“”‘’")

            with self.__filepath.open("r", encoding="utf-8-sig") as file:
                for line in file:
                    cleaned_line: str = line.lower().translate(translator)
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
    
    def print_report(self) -> None:
        """
        Print all words and their frequencies in alphabetical order.
        """
        sorted_words: list[str] = sorted(self.__frequency.keys())

        for word in sorted_words:
            print(f"{word:<25}:: {self.__frequency[word]}")


def file_menu() -> dict[str, Path]:
    """
    Build and return the menu of available files.

    Returns:
        A dictionary mapping menu option strings to file paths.
    """
    base_path: Path = Path(__file__).parent
    file_options: dict[str, Path] = {
        "1": base_path / "monte_cristo.txt",
        "2": base_path / "princess_mars.txt",
        "3": base_path / "Tarzan.txt",
        "4": base_path / "treasure_island.txt",
    }

    return file_options

def display_name(filepath: Path) -> str:
    """
    Convert a file path into a cleaner display name.

    Args:
        filepath: The path of the file.

    Returns:
        A title-cased display name without the file extension.
    """
    return filepath.stem.replace("_", " ").title()
    
def main() -> None:
    """
    Display the menu, process the user's selection, and show the report.
    """
    files: dict[str, Path] = file_menu()
    exit_key: str = str(len(files) + 1) #"5" when there are 4 files, etc.

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")

        for key, filepath in files.items():
            print(f"  {key}. {display_name(filepath)}")
        print(f"  {exit_key}. Exit\n")

        choice: str = input(f"Enter your choice (1-{exit_key}): ").strip()

        if choice == exit_key:
            print("\nGoodbye!")
            break

        if choice not in files:
            print(f"\nInvalid choice. Please select from 1-{exit_key}.")
            input("\nPress Enter to return to the menu... ")
            continue

        filepath: Path = files[choice]
        print(f"\nProcessing '{filepath.name}'...\n")

        analyzer: WordAnalyzer = WordAnalyzer(filepath)
        if analyzer.process_file():
            analyzer.print_report()

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
