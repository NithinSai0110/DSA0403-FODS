def calculate_likes_frequency(likes_list):
    likes_freq = {}  # Dictionary to store the frequency of likes

    # Calculate the frequency of each like count
    for likes in likes_list:
        if likes in likes_freq:
            likes_freq[likes] += 1
        else:
            likes_freq[likes] = 1

    return likes_freq

# Sample dataset containing the number of likes for each post
sample_likes_data = [10, 20, 15, 10, 5, 20, 15, 15, 10, 25, 30]

# Call the function to calculate the frequency distribution
likes_frequency = calculate_likes_frequency(sample_likes_data)

# Print the frequency distribution
print("Likes Frequency Distribution:")
for likes, frequency in sorted(likes_frequency.items()):
    print(f"{likes} likes: {frequency} posts")
