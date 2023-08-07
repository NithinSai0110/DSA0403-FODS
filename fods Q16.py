def calculate_word_frequency(review_text):
    # Convert the text to lowercase for case-insensitive word counts
    review_text = review_text.lower()

    # Tokenize the review into individual words
    words = review_text.split()

    # Remove punctuation and digits from words
    words = [word.strip(".,!?()[]{}-\"'") for word in words if word.isalpha()]

    # Remove stopwords (commonly used words that don't carry much meaning)
    stop_words = set([
        "a", "an", "and", "the", "in", "on", "at", "to", "of", "for", "it", "is", "with", "was", "were", "I", "you", "he", "she", "they", "we"
    ])
    words = [word for word in words if word not in stop_words]

    # Count the frequency of each word using a dictionary
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency

def main():
    # Sample dataset containing customer reviews
    customer_reviews = [
        "This product is amazing. I love it!",
        "The quality is excellent, highly recommended.",
        "Not worth the price. Disappointed with the purchase.",
        "The customer service was terrible, never buying again.",
        "Incredible product. Works as expected.",
        "Great value for money."
    ]

    # Calculate frequency distribution for each review
    total_word_frequency = {}
    for review in customer_reviews:
        review_frequency = calculate_word_frequency(review)
        for word, frequency in review_frequency.items():
            total_word_frequency[word] = total_word_frequency.get(word, 0) + frequency

    # Display the frequency distribution
    print("Frequency Distribution of Words:")
    for word, frequency in total_word_frequency.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
