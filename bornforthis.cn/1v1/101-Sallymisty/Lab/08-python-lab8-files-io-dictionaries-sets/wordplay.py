def read_words(words_file):
    with open(words_file) as f:
        words = [line.strip() for line in f]
    return words

# Task 1
def most_frequent_word_lengths(word_list, top_n):
    # TODO: implement this function
    pass

# Task 2
def first_three_consecutive_double_letters(word_list):
    # TODO: implement this function
    pass

# Task 3a
def most_frequent_bigrams(word_list, top_n):
    # TODO: implement this function
    pass

# Task 3b
def non_present_bigrams(word_list):
    # TODO: implement this function
    pass

if __name__ == "__main__":
    word_list = read_words("wordlist.txt")

    print(most_frequent_word_lengths(word_list, 10))
    print(first_three_consecutive_double_letters(word_list))
    print(most_frequent_bigrams(word_list, 10))
    print(non_present_bigrams(word_list))

