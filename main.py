def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_counts = char_count(text)
    print(f"--- Begin report {book_path} ---")
    print(f"{num_words} words found in the document")
    # print(f"{char_count(text)}")
    print_report(char_counts)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(words):
    split_words = words.split()
    result = len(split_words)
    return result


def char_count(text):
    lowered_string = text.lower()
    char_count_dict = {}

    for char in lowered_string:
        if char.isalpha():
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1
    return char_count_dict


def sort_on(dict_get_key):
    return (dict_get_key["num"])


def print_report(char_counts):
    char_list = [{'char': k, 'num': v} for k, v in char_counts.items()]
    char_list.sort(reverse=True, key=sort_on)

    for entry in char_list:
        print(f"The '{entry['char']}' character was found {entry['num']} time")


main()
