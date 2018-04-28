from api_key import api
from get_suggestions import fetch_suggestions
import time

slug = "technology"


def fetch_test():
    r = api.request("users/suggestions/:" + slug)
    parse_response = r.json()
    users_inf = parse_response["users"]
    for x in users_inf:
        print(x["id_str"])

def make_friendship(UIDS):
    for x in UIDS:
        print(x)
        r = api.request("friendships/create", {"user_id":x})
        print(r.status_code)
        time.sleep(100)
