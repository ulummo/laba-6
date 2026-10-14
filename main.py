def is_pangram(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    return all(letter in text for letter in alphabet)
print(is_pangram("The quick brown fox jumps over the lazy dog"))