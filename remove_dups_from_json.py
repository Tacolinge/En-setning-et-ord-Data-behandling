import json

file = r'C:\Users\fortn\Desktop\Programmerings prosjekter\En Setning Et Ord\data-behandling\En-setning-et-ord-Data-behandling\cleanWordDataBm.json'


def remove_dups_from_json(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        new_data = []
        unique_words = set()
        for item in data:
            word = item.get("Word")

            if word not in unique_words:
                unique_words.add(word)
                new_data.append(item)
            else:
                print("removed dupe:", word)

        with open(file, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=4, ensure_ascii=False)
        print("Removed words complete unique words count: ", len(unique_words))
        f.close
    f.close


remove_dups_from_json(file)
