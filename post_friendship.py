from get_suggestions import fetch_suggestions
from search_to_follow import who_follows, master_ID
import time, json
from TwitterAPI import TwitterAPI

with open("api_key.json") as json_data:
    all_keys = json.load(json_data)
    consumer_key = all_keys["consumer_key"]
    consumer_secret = all_keys["consumer_secret"]
    access_token_key = all_keys["access_token_key"]
    access_token_secret = all_keys["access_token_secret"]

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)


slug = "technology"

IDS_array = who_follows(master_ID)


def make_friendship(UIDS):
    for x in UIDS:
        print(x)
        r = api.request("friendships/create", {"user_id":x})
        print(r.status_code)
        time.sleep(70)
