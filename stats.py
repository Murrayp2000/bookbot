def get_num_words(input_string):
	words = input_string.split()
	word_count = len(words)
	return word_count

def get_appearence_count(input_string):
	char_list = []
	dict = {}
	for char in input_string:
		char = char.lower()
		if char in char_list:
			count = dict[char] + 1
			dict[char] = count
		else:
			char_list.append(char)
			dict[char] = 1
	return dict


