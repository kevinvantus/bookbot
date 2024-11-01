def main():
    contents = read_book_contents('books/frankenstein.txt')
    word_count = count_words(contents)
    print(word_count)


def read_book_contents(path: str):
    with open(path) as f:
        contents = f.read()
        return contents


def count_words(text: str):
    return len(text.split(None))


main()
