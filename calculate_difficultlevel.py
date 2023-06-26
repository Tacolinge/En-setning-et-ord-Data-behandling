import json

# kalkulerer vansklighetsgrad utifra flere ting som frekevs fra avisartiklene,
# om example er ulik null...
# målet er: jo høyere DifficultLevel jo lettere ord.
freq_file = r"C:\Users\fortn\Desktop\Programmerings prosjekter\En Setning Et Ord\data-behandling\En-setning-et-ord-Data-behandling\frequency.json"
word_file = r"C:\Users\fortn\Desktop\Programmerings prosjekter\En Setning Et Ord\data-behandling\En-setning-et-ord-Data-behandling\cleanWordDataBm.json"


def calculate_from_frequency(frequency_file, word_data_file):
    with open(frequency_file, "r", encoding="utf-8") as freq_file:
        frequency_data = json.load(freq_file)

    with open(word_data_file, "r", encoding="utf-8") as word_file:
        word_data = json.load(word_file)

    updated_data = []
    for word_dict in word_data:
        word = word_dict["Word"]
        if word in frequency_data and frequency_data[word] > 10000:
            word_dict["DifficultLevel"] += 12
        if word in frequency_data and frequency_data[word] > 5000:
            word_dict["DifficultLevel"] += 10
        if word in frequency_data and frequency_data[word] > 2500:
            word_dict["DifficultLevel"] += 9
        if word in frequency_data and frequency_data[word] > 1250:
            word_dict["DifficultLevel"] += 8
        if word in frequency_data and frequency_data[word] > 500:
            word_dict["DifficultLevel"] += 7
        if word in frequency_data and frequency_data[word] > 200:
            word_dict["DifficultLevel"] += 5
        if word in frequency_data and frequency_data[word] > 40:
            word_dict["DifficultLevel"] += 3
        if word in frequency_data and frequency_data[word] > 15:
            word_dict["DifficultLevel"] += 2
        if word in frequency_data and frequency_data[word] > 5:
            word_dict["DifficultLevel"] += 1
        updated_data.append(word_dict)

    with open(word_data_file, "w", encoding="utf-8") as update_file:
        json.dump(updated_data, update_file, indent=4, ensure_ascii=False)


def calculate_if_example(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    for word_dict in data:
        if word_dict["example"] is not None:
            word_dict["DifficultLevel"] += 3

    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def calculate_from_word_length(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    # disse stacker så om ordet har 4 tegn blir det 1+1+3
    for word_dict in data:
        if word_dict["WordLength"] >= 15:
            word_dict["DifficultLevel"] -= 2
        if word_dict["WordLength"] >= 10:  # bigger-
            word_dict["DifficultLevel"] -= 1
            continue  # ingen grunn å sjekke de under
        if word_dict["WordLength"] <= 9:  # smaller-
            word_dict["DifficultLevel"] += 1
        if word_dict["WordLength"] <= 8:
            word_dict["DifficultLevel"] += 1
        if word_dict["WordLength"] <= 5:
            word_dict["DifficultLevel"] += 3
        if word_dict["WordLength"] <= 3:
            word_dict["DifficultLevel"] += 2
        if word_dict["WordLength"] <= 2:
            word_dict["DifficultLevel"] += 6

    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def calculate_from_explanation_length(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    for word_dict in data:
        words = word_dict["explanation"].split()  # antall ord i explanation

        if len(words) == 2:
            word_dict["DifficultLevel"] -= 10
        if len(words) == 1:
            word_dict["DifficultLevel"] -= 18
            continue
        if len(words) > 5:
            word_dict["DifficultLevel"] += 1
        if len(words) > 7:
            word_dict["DifficultLevel"] += 1
        if len(words) > 8:
            word_dict["DifficultLevel"] += 1
        if len(words) > 10:
            word_dict["DifficultLevel"] += 2
        if len(words) > 12:
            word_dict["DifficultLevel"] += 2
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# resetter alle levler til 0


def reset_all_difficultlevels(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        for word_dict in data:
            word_dict["DifficultLevel"] = 0
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("resatt alle DifficultLevels til 0")


def run():
    print("starter alle calculate funksjoner")
    calculate_from_frequency(freq_file, word_file)
    print("fra freq Ferdig")
    calculate_if_example(word_file)
    print("if example Ferdig")
    calculate_from_word_length(word_file)
    print("from word length Ferdig")
    calculate_from_explanation_length(word_file)
    print("from explanation Ferdig")
    print("ALL complete")


def sjekk(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        for word_dict in data:
            if word_dict["DifficultLevel"] > 42:
                print("denne har over 42 i Lvl ", word_dict)
            if word_dict["DifficultLevel"] < -10:
                print("denne har under -10 i Lvl ", word_dict)


reset_all_difficultlevels(word_file)
run()
sjekk(word_file)
