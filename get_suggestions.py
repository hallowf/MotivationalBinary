from api_key import api
import json

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
