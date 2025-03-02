import sys
from stats import get_num_words, get_char_count, sort_dictionaries



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    dict = get_char_count(text)
    sorted_list = sort_dictionaries(dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["name"].isalpha():
            print(f"{dict["name"]}: {dict["num"]}")
    print("============= END ===============")


main()