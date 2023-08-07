import string
from collections import Counter

def process_text(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()
    return text.split()

if __name__ == "__main__":
    # Get file name input from the user
    file_name = input("Enter the file name (including extension): ")

    try:
        # Read the text document
        with open(file_name, "r") as file:
            text = file.read()

        # Process the text and calculate the frequency distribution
        words = process_text(text)
        frequency_dict = Counter(words)

        # Display the frequency distribution
        print("Word Frequency Distribution:")
        for word, frequency in frequency_dict.items():
            print(f"{word}: {frequency}")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
