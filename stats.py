# Function to count the number of words in a given text
def word_count(book_text):
    # Use the .split() method to turn the text into a list of words
    # Each word will be a separate item in the list
    words = book_text.split()
    # Use len() to count how many words are in the list
    word_count = len(words)
    return word_count


def letter_count(text):
    lowercase = text.lower()
    letter_counter = {}

    for char in lowercase:
        if char in letter_counter:
            letter_counter[char] += 1
        else:
            letter_counter[char] = 1

    return letter_counter

def sort_character_counts(letter_counter):
    # Create an empty list to hold our dicts
    sorted_list = []

    # Loop over each character and its count in the input dictionary
    for char, count in letter_counter.items():
        # Only include alphabetical characters
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})

    # Define a sorting key function
    def sort_on(item):
        return item["num"]

    # Sort the list in-place from largest to smallest by "num"
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
