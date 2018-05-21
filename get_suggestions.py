import json
from TwitterAPI import TwitterAPI

with open("api_key.json") as json_data:
    all_keys = json.load(json_data)
    consumer_key = all_keys["consumer_key"]
    consumer_secret = all_keys["consumer_secret"]
    access_token_key = all_keys["access_token_key"]
    access_token_secret = all_keys["access_token_secret"]

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

# Category to search users
slug = "tecnologia"

# Find suggestions of users
def fetch_suggestions():
    r = api.request("users/suggestions/:" + slug)
    print(r.status_code)
    parse_response = r.json()
    users_inf = parse_response["users"]
    IDS = {}
    for x in users_inf:
        IDS[x["id_str"]] = x["name"]
    print(IDS)
    return IDS
