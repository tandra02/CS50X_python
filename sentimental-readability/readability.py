from cs50 import get_string


def count_letters(text):
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1
    return letters


def count_words(text):
    words = len(text.split())
    return words


def count_sentences(text):
    # Assume that any sequence of characters that ends with a '.', '!', or '?' is a sentence
    sentences = 0
    for char in text:
        if char in ['.', '!', '?']:
            sentences += 1
    return sentences


text = get_string("Text: ")
letterCount = count_letters(text)
wordCount = count_words(text)
sentenceCount = count_sentences(text)

L = letterCount / wordCount * 100
S = sentenceCount / wordCount * 100
index = 0.0588 * L - 0.296 * S - 15.8

if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {round(index)}")
