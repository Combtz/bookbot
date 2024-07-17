def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()

    num_words = num_of_words(file_contents)
    num_chars = num_of_char(file_contents)
    char_sorted_list = char_dict_to_list(num_chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def num_of_words(s):
    return len(s.split()) 

def num_of_char(s):
    output = {}
    for char in s:
        if char.isalpha():
            char = char.lower()
            if char not in output:
                output[char] = 1
            else:
                output[char] += 1
    return output

def sort_on(dict):
    return dict["num"]

def char_dict_to_list(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char" : ch, "num" : char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list




if __name__ == '__main__':
    main()