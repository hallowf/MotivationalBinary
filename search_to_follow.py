from api_key import api
import json


master_ID = "21447363"

def who_follows(ID):
    page_cursor = -1
    r = api.request("friends/ids", {"user_id":ID, "cursor":page_cursor})
    parse_response = r.json()
    print (parse_response)
    page_cursor += -1
    print(page_cursor)


who_follows(master_ID)
