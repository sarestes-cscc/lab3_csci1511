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
        