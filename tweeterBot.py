from TwitterAPI import TwitterAPI
from get_quote import fetch_random, convert_quote
from post_friendship import make_friendship, IDS_array
import json

with open("api_key.json") as json_data:
    all_keys = json.load(json_data)
    consumer_key = all_keys["consumer_key"]
    consumer_secret = all_keys["consumer_secret"]
    access_token_key = all_keys["access_token_key"]
    access_token_secret = all_keys["access_token_secret"]

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

hex_quote = convert_quote(fetch_random()) + " #hex #joke"

def post_tweet(text):
    r = api.request("statuses/update", {"status":text})
    print(r.status_code)


def follow_request(user):
    make_friendship(user)


post_tweet(hex_quote)

follow_request(IDS_array)
