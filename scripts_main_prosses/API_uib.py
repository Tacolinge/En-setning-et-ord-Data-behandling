# kaller på uib sin ordbok api for å hente ut blant annet example og exlanation
import requests

json_path = r"test_lemma_til_api.json"

new_json_data = []  # list of dicts


def get_article_url(article_id):
    api_url = "https://ord.uib.no/bm/article/"
    file_json = ".json"
    url = api_url + str(article_id) + file_json
    return url


def uib_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()  # dict
        return json_data
    else:
        print("ERROR ", response.status_code, url)
