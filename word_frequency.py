import sys




def word_frequency(given_string):
	"""Takes a string, returns a dictionary with the
	count for each word in the string"""
	word_dict = {}
	clean_line = given_string
	for character in "-!.,#*[]_()\':;?/@:\"":
		clean_line = clean_line.replace(character," ")
	clean_line = clean_line.lower()
	our_words = clean_line.split()
	for word in our_words:
		word_dict[word] = (word_dict.get(word, 0) + 1)
	return word_dict

def gets_count(dictionary_item):
	"""Returns the second item in a tuple"""
	return dictionary_item[1]

our_dict = {}

default_text = "sample.txt"

if len(sys.argv) > 1:
	source_file = sys.argv[1]
else:
	source_file = default_text

with open(source_file) as our_file:
	our_text = our_file.readlines()
	for our_line in our_text:
		midway_dict = word_frequency(our_line)
		for key in midway_dict:
			our_dict[key] = midway_dict[key] + our_dict.get(key, 0)

dict_list = our_dict.items()
sorted_dict_list = sorted(dict_list, key=gets_count, reverse=True)
top_twenty = sorted_dict_list[:20]

# for word, count in top_twenty:
#	print("{} {}".format(word.ljust(10), count))

def fancy_histogram(given_list, count=20):
	"""Prints a normalized histogram to the terminal of the top 20 items in a
	sorted list of word/count tuples"""
	largest_count = given_list[0][1]
	normalized_list = []
	for item in range(count):
		normalized_key_count = (50 * given_list[item][1]) // largest_count
		normalized_list.append((given_list[item][0],"#"*normalized_key_count))
	for pair in normalized_list:
		print("{} {}".format(pair[0].ljust(10), pair[1]))

fancy_histogram(sorted_dict_list)
