import json


def nested_values_explanation(data, type_):
    while not data.get("type_") == type_:
        if "elements" in data.keys():
            data = data["elements"][0]
    if "$" in data["content"]:  # hvis den inneholder $ retuner dict
        return data
    return data["content"]


def nested_values_example(data, type_):  # Spaghetti :)
    while not data.get("type_") == type_:
        if "elements" in data:
            print("elements in data")
            # sjekk om det er nested nivå til
            print("1--")
            for i in data["elements"]:
                print("2------", i)
                if not i.get("type_") == type_:
                    data = data["elements"]
                    continue
                print("blir denne kalt????????????")
                data = i  # dict der type_ finnes i, kan også inneholde flere nøstede dicts
                break
            print("en runde i for loop")

    if "$" in data["quote"]["content"]:  # hvis den inneholder $ retuner dict
        return data
    return data["quote"]["content"]


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
    word = json_data["lemmas"][0]["lemma"]
    definitions = json_data["body"]["definitions"][0]
    explanation = find_dict_with_type(definitions, "explanation")
    example = find_dict_with_type(definitions, "example")
    print("Output", '\n')
    print(word, explanation, example, sep='\n')
    print('\n')


""" def run(json_file):
    f = open(json_file, encoding='utf-8')
    data = json.load(f)
    collect_values(data) """
