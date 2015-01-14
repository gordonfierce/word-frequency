
def word_frequency(given_string):
	word_dict = {}
	clean_line = given_string
	for character in "-!.,#*()\':;?/@:\"":
		clean_line = clean_line.replace(character," ")
	clean_line = clean_line.lower()
	our_words = clean_line.split()
	for word in our_words:
		word_dict[word] = (word_dict.get(word, 0) + 1)
	return word_dict


with open("sample.txt") as our_file:
	our_text = our_file.readlines()
	our_dict = {}
	for our_line in our_text:
		midway_dict = word_frequency(our_line)
		for key in midway_dict:
			our_dict[key] = midway_dict[key] + our_dict.get(key, 0)

def gets_count(dictionary_item):
	return dictionary_item[1]

dict_list = our_dict.items()
sorted_dict_list = sorted(dict_list, key=gets_count, reverse=True)
top_twenty = sorted_dict_list[:20]

for word, count in top_twenty:
	print "{} {}".format(word, count)
