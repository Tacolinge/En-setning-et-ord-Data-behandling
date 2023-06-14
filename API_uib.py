import requests
import time

def make_article_num(number):
    counter = 0
    while counter < number:
        counter += 1
        #print(counter)
        get_article_url(counter)

def get_article_url(article_id):
    api_url = "https://ord.uib.no/bm/article/"
    file_json = ".json"
    url = api_url + str(article_id) + file_json
    print(url)

#test = requests.get("https://ord.uib.no/bm/article/1.json")


if __name__ == "__main__":
    start_timer = time.time()
    make_article_num(100)
    get_article_url(1)

    end_timer = time.time()
    print(end_timer - start_timer)