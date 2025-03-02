from stats import get_num_words, get_char_count


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)

    print(f"{num_words} words found in the document")
    print(get_char_count(text))


main()