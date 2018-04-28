import pickle

def reset_pickle_template():
    with open("objs.pkl.template", "wb") as f:
        pickle.dump(-1, f)


def reset_pickle():
    with open("objs.pkl", "wb") as f:
        pickle.dump(-1, f)


def get_pickle():
    with open("objs.pkl", "rb") as f:
        obj = pickle.load(f)
        print(obj)
        return obj


def get_pickle_template():
    with open("objs.pkl.template", "rb") as f:
        obj = pickle.load(f)
        print(obj)
        return obj


reset_pickle_template()
reset_pickle()

get_pickle_template()
get_pickle()
