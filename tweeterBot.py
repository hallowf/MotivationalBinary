from api_key import api

bruh = "Lil wayne"

def post_tweet(text):
    r = api.request('statuses/update', {'status':text})
    print(r.status_code)


post_tweet(bruh)
