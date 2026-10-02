sentence = input("Enter a sentence: ")

if sentence.strip() == "":
    print("Please enter a sentence.")
else:
    word_count = len(sentence.split())
    character_count = len(sentence)

    print("Word count:", word_count)
    print("Character count:", character_count)