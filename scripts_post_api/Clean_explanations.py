import json
import scripts_main_prosses.collect_values as cv
file = r'cleanWordDataBm.json'


# for å luke ut ord uten fullstndig forklaring
def clean_explanations(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        keep_data = []
        counter = 0
        ord = []
        for e in data:
            if isinstance(e["explanation"], dict):
                ny_verdi = cv.make_missing_word_list(e["explanation"])
                if not isinstance(ny_verdi, str):
                    counter += 1
                    ord.append(e["Word"])
                    continue
                e["explanation"] = ny_verdi
            keep_data.append(e)
    with open("cleanWordDataBm.json", "w", encoding="utf-8") as new_file:
        json.dump(keep_data, new_file, indent=4,
                  ensure_ascii=False, sort_keys=True)
    f.close
    print(ord, counter, len(keep_data), sep='\n')


def clean_explanations_strings(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        keep_data = []
        for e in data:
            if e["example"] != None:
                if not "$" in e["example"]:
                    keep_data.append(e)
                if "$" in e["example"]:
                    e["example"] = None
                    print(e["example"])
            keep_data.append(e)
    with open("cleanWordDataBm.json", "w", encoding="utf-8") as new_file:
        json.dump(keep_data, new_file, indent=4,
                  ensure_ascii=False, sort_keys=True)


def check(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        print(len(data))
