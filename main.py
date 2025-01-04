import os


def get_book_text(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        raise e


def sort_on(dict):
    return dict["num"]


def count_character(text):
    appear_characters = {}
    words = text.split()

    for word in words:
        for character in word:
            if character.isalpha():
                lowercase_char = character.lower()
                appear_characters[lowercase_char] = (
                    appear_characters.get(lowercase_char, 0) + 1
                )

    character_count = []
    for character in appear_characters:
        character_count.append({"name": character, "num": appear_characters[character]})

    character_count.sort(reverse=True, key=sort_on)
    return len(words), character_count


def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")

    file_path = os.path.join(os.getcwd(), book_path)
    text = get_book_text(file_path)
    if text:
        count_words, appear_characters = count_character(text)

    print(f"{count_words} words found in the document")

    print()
    for character in appear_characters:
        print(f"The '{character['name']}' character was found {character['num']} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()
