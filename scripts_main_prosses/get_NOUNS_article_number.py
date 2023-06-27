import json
import re


# Dette er et script som tar inn lemma.json, uthenter Substantivene og skriver en ny json-fil.
# kan endres til andre ordklasser seinere om behov
# denne filen finner artkkel nummer til alle substantivene så de kan brukes til å kalle på uib-api'en


data_ny_json = []
unike_ord = set()

find_path_to_lemma = "lemma.json"


def check_regex_match(word, regex_expressions):
    for exp in regex_expressions:
        if not re.search(exp, word):
            continue
        else:
            return False  # match som betyr ordet kan IKKE brukes
    return True  # ingen re match ordet kan brukes

# fjerner duplikater og ord som ikke er substantiv


def clean_up_json(json_file):
    regex_expressions = [
        r'^-',
        r'\d',
        r'^.$',
        r'-'
    ]
    f = open(json_file)
    data = json.load(f)
    for i in data:  # struktur på listen er ["ordet", artikkelnr, "ordklasse"]
        if "NOUN_regular" in i[2]:
            if check_regex_match(i[0], regex_expressions):
                if i[0] not in unike_ord:
                    unike_ord.add(i[0])
                    data_ny_json.append(i)
    f.close

# Lager ny json fil, med "ordet", artikkel nr. og "ordklasse"


def write_json(ny_data, filename='lemma_nouns.json'):
    json_obj = json.dumps(ny_data, indent=4, sort_keys=True)
    with open(filename, 'w') as file:
        file.write(json_obj)


def run():
    clean_up_json(find_path_to_lemma)  # Henter ut og behandler data
    write_json(data_ny_json)  # Skriver ny data til fil
    print("Complete! Antall i set: ", len(unike_ord))
