"""
main() function 

"""

print ("--- Word Analyzer ---")
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