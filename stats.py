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
