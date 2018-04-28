from api_key import api
import json
import pickle

master_ID = "21447363"

def who_follows(ID):
    page_cursor = get_pickle()
    r = api.request("friends/ids", {"user_id":ID, "cursor":page_cursor})
    parse_response = r.json()
    users_ids = parse_response["ids"]
    IDS = []
    for x in users_ids:
        IDS.append(x)
    page_cursor += -1
    make_pickle(page_cursor)
    print(IDS)
    return IDS

def reset_pickle_template():
    with open("objs.pkl.template", "wb") as f:
        pickle.dump(-1, f)


def reset_pickle():
    with open("objs.pkl", "wb") as f:
        pickle.dump(-1, f)

def make_pickle(obj):
    with open("objs.pkl", "wb") as f:
        pickle.dump(obj, f)

def get_pickle():
    with open("objs.pkl", "rb") as f:
        obj = pickle.load(f)
        print(obj)
        return obj
