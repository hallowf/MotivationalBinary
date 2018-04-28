from api_key import api
from get_quote import fetch_random
from get_quote import convert_quote
from post_friendship import make_friendship
from post_friendship import IDS_array

hex_quote = convert_quote(fetch_random()) + " #hex #joke"

def post_tweet(text):
    r = api.request("statuses/update", {"status":text})
    print(r.status_code)


def follow_request(user):
    make_friendship(user)


post_tweet(hex_quote)

follow_request(IDS_array)
