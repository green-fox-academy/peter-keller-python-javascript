word1_input = input("Insert info: ")
word2_input = input("Another info: ")

def anagram_length(word1 , word2):
    if sorted(word1) == sorted(word2):
        print("Guess I am an anagram, no big deal")
    else:
        print("Move along, nothing to see here")
anagram_length(word1_input, word2_input)