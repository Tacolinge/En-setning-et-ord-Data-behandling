#import requests
import time
import json
import os

#find_path_to_json_file = os.getcwd() + "\test_lemma_til_api.json"
relative_path = "En-setning-et-ord-Data-behandling\test_lemma_til_api.json"
def get_article_url(article_id):
    api_url = "https://ord.uib.no/bm/article/"
    file_json = ".json"
    url = api_url + str(article_id) + file_json
    print(url)

#test = requests.get("https://ord.uib.no/bm/article/1.json")


def get_article_number(json_file):
    f = open(json_file)
    data = json.load(f)
    for i in data:          #struktur på listen er ["ordet", artikkelnr, "ordklasse"]
        get_article_number(i[1])
    
    f.close





if __name__ == "__main__":
    start_timer = time.time()
    os.getcwd()

#    get_article_number(relative_path)

    end_timer = time.time()
    print(end_timer - start_timer)
