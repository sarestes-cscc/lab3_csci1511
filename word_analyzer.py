"""
Word Analyzer Module
Sarah Estes
To analyze words and word count in different text files.
pathlib and string libraries used
9/30/26
"""

from pathlib import Path
import string

class WordAnalyzer:
    """Word Analyzer class used to analyze words and word count"""
    def __init__(self, file_path):
        """Initialize WordAnalyzer with a file path"""
        self.file_path = Path(file_path)
        self.word_count = {"word": "", "count": ""}

    def process_file(self, file_path):
        """Contains the program's main logic"""
        path = Path(file_path)
        try:
            contents = self.path.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"I'm sorry, {file_path} was not found.")
            return
        
        contents = path.open()
        for line in contents:
            line = line.translate(str.maketrans('', '', string.punctuation))
            line = line.lower()
            return line 

            words = contents.split()
            counter = 0
            for word in words:
                self.word_count["word"] = word
                if word in self.word_count:
                    counter += 1
                    self.word_count["count"] = counter
            return self.word_count

    def print_report(self):
        """Prints the word counter results"""
        sorted_word_count = dict(sorted(self.word_count.items()))
        for key, value in sorted_word_count.items():
            print(f"{key} :: {value}")