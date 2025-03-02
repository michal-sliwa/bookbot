def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_dictionaries(dict):
    list = []
    for key in dict:
        list.append({"name": key, "num": dict[key]})

    list.sort(reverse=True, key=sort_on)
    return list
    