def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    return len(text.split())


def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)

    print(f"{num_words} words found in the document")


main()