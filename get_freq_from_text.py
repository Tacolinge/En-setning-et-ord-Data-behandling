import string
import json
import time
import re

file = r"C:\Users\fortn\Desktop\Programmerings prosjekter\En Setning Et Ord\data-behandling\En-setning-et-ord-Data-behandling\text_to_check_frequency.txt"
new_file = "frequency.json"

regex_expressions = [
    r'\d',
    r'^.$',
]


def remove_punctuations(line):
    for char in string.punctuation:
        line = line.replace(char, "")
    return line


def check_singel_char(word):
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


def run(file):
    start_timer = time.time()
    word_count = add_words_from_file(file)
    write_json(word_count, new_file)
    end_timer = time.time()
    print("Completed in: ", end_timer - start_timer)


run(file)
