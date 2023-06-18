import json
import os
import time
import requests

# find_path_to_json_file = os.getcwd() + "\test_lemma_til_api.json"
json_path = r"En-setning-et-ord-Data-behandling\test_lemma_til_api.json"

new_json_data = []  # list of dicts


def collect_values(json_data):
    word = json_data["lemmas"][0]["lemma"]
    explanation = json_data["body"]["definitions"][0]["elements"][0]["elements"][0]["content"]
    example = json_data["body"]["definitions"][0]["elements"][0]["elements"][1]["quote"]["content"]
    print(word, explanation, example, sep='\n')


def get_article_url(article_id):
    api_url = "https://ord.uib.no/bm/article/"
    file_json = ".json"
    url = api_url + str(article_id) + file_json
    # print(url)
    return url


def uib_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()  # dict
        return json_data
        # for keys in json_data:
        #    print(keys)
    else:
        print("ERROR ", response.status_code, url)


def get_article_number(json_file):
    # word_id_counter = 0
    f = open(json_file, encoding='utf-8')
    data = json.load(f)
    # struktur på listen er ["ordet", artikkelnr, "ordklasse"]
    for num in data:
        url = get_article_url(num[1])
        json_data = uib_api(url)
        # print(json_data)
        collect_values(json_data)
    f.close


if __name__ == "__main__":
    start_timer = time.time()
    get_article_number(json_path)  # runs the app
    # uib_api("https://ord.uib.no/bm/article/1.json")
    end_timer = time.time()
    print(end_timer - start_timer)
