from stats import word_count
from stats import letter_count
from stats import sort_character_counts
import sys


# Set the relative path to the text file containing the book
# filepath = "books/frankenstein.txt"

# Define a function that takes a file path and returns the full text inside the file
def get_book_text(filepath):
    # Open the file using a context manager (with block)
    # This ensures the file is properly closed after reading
    with open(filepath) as f:
        # Read the entire contents of the file into a single string
        contents = f.read()

    return contents

# Define the main function to control the flow of the program
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    words = word_count(text)
    character_counts = letter_count(text)
    sorted_characters = sort_character_counts(character_counts)

    print(f"Found {words} total words")
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")

    print(sorted_characters)

    print(character_counts)


main()
