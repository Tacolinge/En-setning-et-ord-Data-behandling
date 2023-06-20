# -Runs the api_uib with json file
# -Collects word data
# -Write's to new json file

import json
import API_uib as api
import collect_values as cv
import time

json_path = "test_lemma_til_api.json"


def main(json_file):
    # word_id_counter = 0
    f = open(json_file, encoding='utf-8')
    data = json.load(f)
    # struktur på listen er ["ordet", artikkelnr, "ordklasse"]
    for num in data:
        url = api.get_article_url(num[1])
        json_data = api.uib_api(url)
        values = cv.collect_values(json_data)
        # print(values, "her er values")
    f.close


if __name__ == "__main__":
    start_timer = time.time()
    main(json_path)
    end_timer = time.time()
    print("completed in: ", end_timer - start_timer)
