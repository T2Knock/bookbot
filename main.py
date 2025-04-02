import os
import sys

from stats import count_character


def get_book_text(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        raise e


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    count_words = 0
    appear_characters = {}

    print(f"--- Begin report of {book_path} ---")

    file_path = os.path.join(os.getcwd(), book_path)
    text = get_book_text(file_path)
    if text:
        count_words, appear_characters = count_character(text)

    print(f"{count_words} words found in the document")

    print()
    for character in appear_characters:
        print(f"{character['name']}: {character['num']}")

    print("--- End report ---")


if __name__ == "__main__":
    main()
