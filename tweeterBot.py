from api_key import api
from get_quote import fetch_random
from get_quote import convert_quote

binary_quote = convert_quote(fetch_random())

def post_tweet(text):
    r = api.request("statuses/update", {"status":text})
    print(r.status_code)


post_tweet(binary_quote)
