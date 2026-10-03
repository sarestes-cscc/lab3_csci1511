"""
main() function 

"""
from word_analyzer import WordAnalyzer

print ("\n--- Word Analyzer ---")
print("Please select a file to analyze:")

text_options = {
    "1": "The Count of Monte Cristo",
    "2": "A Princess of Mars",
    "3": "Tarzan of the Apes",
    "4": "Treasure Island",
    "5": "Exit",
}

for option, text in text_options.items():
    print(f"{option}: '{text}'")

while True:
    user_choice = input("\nEnter your choice (1-6): ")

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

    else:
        print("Invalid input. Please retry.")
