import json

# strukturer daten som kommer fra main.py og skriver dataen til en json fil


def add_to_dict(new_data):
    formatted_data = []
    for i in new_data:
        wor_len = len(i[1])  # legger til lengden på ordet
        lvl = 0  # setter defualt vanskelighetsgrad
        formatted_data.append({"WordId": i[0], "Word": i[1],
                               "explanation": i[2], "example": i[3],
                               "WordLength": wor_len, "DifficultLevel": lvl})
    return formatted_data


def write_to_json(formatted_data, filename):
    json_obj = json.dumps(formatted_data, indent=4,
                          sort_keys=True, ensure_ascii=False)
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json_obj)


def run_write_json(new_data, filename):
    formatted_data = add_to_dict(new_data)
    write_to_json(formatted_data, filename)
    return True
