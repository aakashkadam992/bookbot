from stats import count_words, get_character_count, get_dict_sorted
import sys 

def get_book_text(f_path):
    with open(f_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    string_output = get_book_text(sys.argv[1])
    count = len(count_words(string_output))
    char_list = get_dict_sorted(get_character_count(string_output))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for i in char_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    #print(char_list)
    print("============= END ===============")


main()