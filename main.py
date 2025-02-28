from stats import get_num_words, count_characters, sorted_list_of_chars
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        f_contents = f.read()
        return f_contents
    
def main():
    if not len(sys.argv) == 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        file_text = get_book_text(file_path)
        file_words = get_num_words(file_text)
        file_count = count_characters(file_text)
        print(f"""============ BOOKBOT ============\nAnalyzing book found at {file_path}...\n----------- Word Count ----------""")
        print(f"Found {file_words} total words")
        print('--------- Character Count -------')
        print(sorted_list_of_chars(file_count))
    
main()