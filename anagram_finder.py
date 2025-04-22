def anagram_finder (s ,t):
    return sorted(s) == sorted(t)

if __name__ == "__main__":

    # Get user input
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    # Check if the words are anagrams
    if anagram_finder(word1, word2):
        print(f"{word1} and {word2} are anagrams.")
    else:
        print(f"{word1} and {word2} are not anagrams.")
            