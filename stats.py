def get_number_of_words(booktext):
    number_of_words = booktext.split()
    return number_of_words

def get_word_count(booktext):
    all_lower_cases = booktext.lower()
    char_number_dict = {}

    for char in all_lower_cases:
        if char not in char_number_dict:
            char_number_dict[char] = 1
        else:
            char_number_dict[char] += 1

    return char_number_dict

def sort_dict(diction):
    sorted_list = []
    for char, num in diction.items():
        new_dict = {"char": char, "num": num}
        sorted_list.append(new_dict)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(items):
    return items["num"]