from stats import get_number_of_words, get_word_count, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    else:
        text = get_book_text(sys.argv[1])
        number = len(get_number_of_words(text))
    
        word_test = get_word_count(text)

        sorted_dict = sort_dict(word_test)


        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {number} total words")
        print("--------- Character Count -------")
        for item in sorted_dict:
            ch = item["char"]
            if ch.isalpha():
                print(f"{ch}: {item['num']}")
        print("============= END ===============")

main()