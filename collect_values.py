import json

relation_dictionary = {"el": "eller", "e_l": "eller lignende"}


def find_relation(value):
    if not value in relation_dictionary.keys():
        print("!!!!!!!!!!!!!! ", value, "DENNE FINNES IKKE I RD!!!!!!!!!")
        return None
    rd_value = relation_dictionary[value]
    return rd_value


def replace_missing_word(text, missing_words_list):
    replaced_string = text
    for replacement in missing_words_list:
        replaced_string = replaced_string.replace("$", replacement, 1)
    return replaced_string


def make_missing_word_list(dictionary):
    keys = dictionary.keys()
    text = ""
    m_words = []
    if "content" in keys:
        text = dictionary["content"]
        for i in dictionary["items"]:
            if "lemmas" in i.keys():
                x = i["lemmas"][0]["lemma"]
                m_words.append(x)
            if "text" in i.keys():
                m_words.append(i["text"])
            if "id" in i.keys():
                for key in i.keys():
                    if key == "id":
                        rel_id = find_relation(i["id"])
                        if not rel_id == None:
                            m_words.append(rel_id)
    if "quote" in keys:
        text = dictionary["quote"]["content"]
        for i in dictionary["quote"]["items"]:
            m_words.append(i["text"])
    if not m_words:  # sjekker om listen er tom
        print("Kunne ikke finne manglende ord.")
        return dictionary
    string = replace_missing_word(text, m_words)
    return string


def parse_dict(dict_to_parse):
    if not isinstance(dict_to_parse, dict):
        # print("IS NOT DICT ", dict_to_parse)
        return None
    keys = dict_to_parse.keys()
    if "content" in keys:
        string = dict_to_parse["content"]
    if "quote" in keys:
        string = dict_to_parse["quote"]["content"]
    if "$" in string:  # må lage en replace funksjon her siden mange ord er linket med "$"
        # replace_missing_word(dict_to_parse)
        string = make_missing_word_list(dict_to_parse)
    return string  # om det ikke går å ersatte $ retuner den dict_to_parse


def find_dict_with_type(data, type_):  # chatGPT to the rescue
    if isinstance(data, dict):
        if "type_" in data and data["type_"] == type_:
            return data
        for value in data.values():
            if isinstance(value, (dict, list)):
                result = find_dict_with_type(value, type_)
                if result is not None:
                    return result
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                result = find_dict_with_type(item, type_)
                if result is not None:
                    return result
    return None


def collect_values(json_data):
    definitions = json_data["body"]["definitions"]
    if not definitions:
        print("Hopper over ordet fordi listen er tom")
        return None
    definitions = json_data["body"]["definitions"][0]
    word = json_data["lemmas"][0]["lemma"]
    # print("DETTE ER DEF_______", definitions, type(definitions))
    explanation = find_dict_with_type(definitions, "explanation")
    example = find_dict_with_type(definitions, "example")
    explanation = parse_dict(explanation)
    example = parse_dict(example)
    if explanation == None:
        print("dropper ", word, "pga ingen forklaring")
        return None
    print("Added WORD_____ ", word)
    return [word, explanation, example]


# teststr = "$ av typen $ med utpreget smak av $"
# test_liste = ["aw"]
