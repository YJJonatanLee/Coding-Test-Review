from collections import Counter

word = str(input()).upper()

word_counter = Counter(word)
word_list = list(word_counter.keys())
word_num_list = list(word_counter.values())

if word_num_list.count(max(word_num_list)) >= 2:
    print('?')
else:
    most_common_word = word_list[word_num_list.index(max(word_num_list))]
    print(most_common_word)
