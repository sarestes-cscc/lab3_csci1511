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
            contents = path.read_text()
        except FileNotFoundError:
            print(f"I'm sorry {file_path} was not found. Please try a different file.")
        
        if path.exists():
            contents = path.open()

        
        