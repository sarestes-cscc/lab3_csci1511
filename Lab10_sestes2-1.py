"""
Word Analyzer Module
Sarah Estes
To analyze words and word count in different text files.
WordAnalyzer Class used from same directory
9/30/26

"""
from word_analyzer import WordAnalyzer

text_options = {
    "1": "The Count of Monte Cristo",
    "2": "A Princess of Mars",
    "3": "Tarzan of the Apes",
    "4": "Treasure Island",
    "5": "Exit",
}

# Taking user choice from input and assigning the file 
# name to user choice to use with method calls
while True:
    print ("\n--- Word Analyzer ---")
    print("Please select a file to analyze:")
    for option, text in text_options.items():
        print(f"{option}: '{text}'")
    
    user_choice = input("\nEnter your choice (1-6): ")

    if user_choice not in text_options:
        print("Invalid input. Please re-enter choice.")
        
    if user_choice == "1":
        file_path = "monte_cristo.txt"
        print(f"\nProcessing '{file_path}'")
        analyzer = WordAnalyzer(file_path)
        analyzer.process_file()
        analyzer.print_report()

    if user_choice == "2":
        file_path = "princess_mars.txt"
        print(f"\nProcessing '{file_path}'")
        analyzer = WordAnalyzer(file_path)
        analyzer.process_file()
        analyzer.print_report()

    if user_choice == "3":
        file_path = "Tarzan.txt"
        print(f"\nProcessing '{file_path}'")
        analyzer = WordAnalyzer(file_path)
        analyzer.process_file()
        analyzer.print_report()

    if user_choice == "4":
        file_path = "treasure_island.txt"
        print(f"\nProcessing '{file_path}'")
        analyzer = WordAnalyzer(file_path)
        analyzer.process_file()
        analyzer.print_report()

    if user_choice == "5":
        break

print("Goodbye!")