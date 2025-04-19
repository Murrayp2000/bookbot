from stats import get_num_words, get_appearence_count
import sys
 
def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
	return file_contents
def get_word_count(text_string):
	word_list = text_string.split()
	word_count = len(word_list)
	return word_count

def main(path):
	book_text = get_book_text(path)
	book_word_count = get_num_words(book_text)
	book_char_apperance = get_appearence_count(book_text)
	structured_print(path,book_word_count,book_char_apperance)

def structured_print(path,word_count,char_dict):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for keys,values in char_dict.items():
		print(f"{keys}: {values}")

def sys_argv_check():
	argv_list = sys.argv
	if len(argv_list) == 1:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		main(argv_list[1])

sys_argv_check()
