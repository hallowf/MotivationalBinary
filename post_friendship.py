from api_key import api
from get_suggestions import fetch_suggestions
import time
from search_to_follow import who_follows
from search_to_follow import master_ID

slug = "technology"

IDS_array = who_follows(master_ID)


def make_friendship(UIDS):
    for x in UIDS:
        print(x)
        r = api.request("friendships/create", {"user_id":x})
        print(r.status_code)
        time.sleep(100)
