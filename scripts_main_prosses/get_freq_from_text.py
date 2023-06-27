import string
import json
import time
import re

file = r"text_to_check_frequency.txt"
new_file = "frequency.json"

punctuation = "!#$%&'()*+,-–—./:;<=>?@[\]^_`{|}~„”“’‘«»БбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯяь"

regex_expressions = [
    r'\d',
    r'^.$',
]


def remove_punctuations(line):
    for char in punctuation:
        line = line.replace(char, " ")
    return line


def check_singel_char(word): #fjerner tall og single bokstaver
    for ex in regex_expressions:
        if re.search(ex, word):
            return False
    return True


def write_json(data_dict, new_file):
    json_obj = json.dumps(data_dict, indent=4,
                          sort_keys=True, ensure_ascii=False)
    with open(new_file, "w", encoding="utf-8") as f:
        f.write(json_obj)


def add_words_from_file(file):
    word_count = {}
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            line = remove_punctuations(line)
            words = line.split()

            for word in words:
                word = word.lower()
                if check_singel_char(word):
                    if word not in word_count:
                        word_count[word] = 0
                    word_count[word] += 1
    return word_count

def delete_low_freq_words(data_dict):
    keys_to_delete = []
    for key in data_dict:
        if data_dict[key] < 5:
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del data_dict[key]
    write_json(data_dict, new_file)
    print("slettet ord under 5 forekomster antall: ", len(keys_to_delete))


def order_dict(file):
    data_dict = open_file_to_get_dict(file)
    sorted_values = []
    for key in data_dict:
        sorted_values.append((data_dict[key], key))
    sorted_values = sorted(sorted_values)
    sorted_values = sorted_values[::-1] #flipper listen så størst kommer først
    return sorted_values

def print_sorted(file):
    most_freq = order_dict(file)[:1000] #antall som printes ut
    for freq in most_freq:
        count, word = freq
        print("{0:15}{1:8d}".format(word, count))


def open_file_to_get_dict(file):
    with open(file, "r", encoding="utf-8") as f:
        data_dict = json.load(f)
    return data_dict



def run(file):
    start_timer = time.time()
    print("running...")
    word_count = add_words_from_file(file)
    write_json(word_count, new_file)
    end_timer = time.time()
    print("Completed in: ", end_timer - start_timer)


#run(file)




