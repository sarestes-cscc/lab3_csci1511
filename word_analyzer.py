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
        self.word_count = {}

    def process_file(self):
        """Contains the program's main logic"""
        try:
            contents = self.file_path.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"I'm sorry, {self.file_path} was not found.")
            return
        
        alter_text = contents.translate(str.maketrans('', '', string.punctuation))
        alter_text = alter_text.lower()
        words = alter_text.split()
        
        for word in words:
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1

    def print_report(self):
        """Prints the word counter results"""
        sorted_word_count = dict(sorted(self.word_count.items()))
        for key, value in sorted_word_count.items():
            print(f"{key} :: {value}")