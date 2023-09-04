
fileName = "books/frankenstein.txt"

def count_letters(content):
    word_dict = {}
    for word in content:
        for letter in word.lower():
            if word_dict.get(letter) is None:
                word_dict[letter] = 1
            else:
                word_dict[letter] += 1
    return word_dict


with open(fileName) as f:
    file_contents = f.read()
    words = file_contents.split()
    letters = count_letters(words).items()
    sorted_letters = sorted(letters, key=lambda a:a[1], reverse=True)
    print(f"--- Begin report of {fileName} ---")
    print(f"{len(words)} found in the document")
    print()
    for letter in sorted_letters:
        if letter[0].isalpha():
            print(f"The '{letter[0]}' character was found {letter[1]} times")

    print("--- End report ---")
