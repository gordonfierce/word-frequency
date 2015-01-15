import sys
from word_frequency import word_frequency
from word_frequency import fancy_histogram
from word_frequency import get_sorted_list
from word_frequency import grab_text


def word_total(given_dict):
    count = 0
    for key in given_dict:
        count += given_dict[key]
    return count


def relative_count_dict(first_dict, second_dict):
    """Given two dictionaries, return a dictionary with the word frequency of
    the first normalized to the average of both."""
    first_count = word_total(first_dict)
    second_count = word_total(second_dict)
    print ("First file has: {} Second file has: {}".format(first_count, second_count))
    average_dict = {}
    for key in first_dict:
        #print("Initially {} is {}".format(key, first_dict[key]))
        first_dict[key] = float(first_dict[key])/float(first_count)
        #print("New normalized key for {} is {}".format(key, first_dict[key]))
    for key in second_dict:
        second_dict[key] = float(second_dict[key])/float(second_count)
    #print second_dict
    for key in first_dict:
        average_dict[key] = first_dict[key] + average_dict.get(key, 0)
    for key in second_dict:
        average_dict[key] = second_dict[key] + average_dict.get(key, 0)
    for key in average_dict:
        average_dict[key] = average_dict[key] / 2
    proportion_dict = {}
    for key in average_dict:
        proportion_dict[key] = first_dict.get(key, 0) - average_dict[key]

    return proportion_dict

text_1 = grab_text(sys.argv[1])
text_2 = grab_text(sys.argv[2])

text_1_disproportionate = relative_count_dict(text_1, text_2)
text_1_dis_list = get_sorted_list(text_1_disproportionate)
#print(text_1_dis_list)

fancy_histogram(text_1_dis_list)
