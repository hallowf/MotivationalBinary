from TwitterAPI import TwitterAPI

with open("api_key.json") as json_data:
    all_keys = json.load(json_data)
    consumer_key = all_keys["consumer_key"]
    consumer_secret = all_keys["consumer_secret"]
    access_token_key = all_keys["access_token_key"]
    access_token_secret = all_keys["access_token_secret"]

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

def check_rate_limit():
    r = api.request("application/rate_limit_status")
    parse_response = r.json()
    resources = parse_response["resources"]
    followers = resources["followers"]
    followers_id = followers["/followers/ids"]
    remaining_req = followers_id["remaining"]
    reset_timer = followers_id["reset"]
    print(followers_id)
    print("Remaining requests: " , remaining_req)
    print("Time until reset: " , reset_timer)


def check_rate_limit_short():
    r = api.request("application/rate_limit_status")
    parse_response = r.json()
    resources = parse_response["resources"]["followers"]["/followers/ids"]["remaining"]
    print("Remaining requests: " , resources)


# check_rate_limit()
# check_rate_limit_short()
