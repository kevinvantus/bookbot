from curses.ascii import isalpha


def main():
    text = read_book_contents('books/frankenstein.txt')
    word_count = count_words(text)
    character_dict = count_characters(text)
    sorted = sort_characters(character_dict)
    print_report(word_count, sorted)


def read_book_contents(path):
    with open(path) as f:
        contents = f.read()
        return contents


def count_words(text):
    return len(text.split(None))


def count_characters(text):
    characters: dict[str, int] = {}
    text = text.lower()

    for c in text:
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1
    return characters


def sort_on(dict):
    return dict['count']


def sort_characters(chars):
    chars_list = []

    for c in chars:
        if c.isalpha():
            chars_list.append({"letter": c, "count": chars[c]})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list


def print_report(total_words, chars):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document\n")

    for c in chars:
        print(f"The '{c['letter']}' character was found {c['count']} times")
    print(f"--- End report ---")


main()
