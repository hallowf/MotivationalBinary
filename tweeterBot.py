from api_key import api


def post_tweet(text):
    r = api.request('statuses/update', {'status':text})
    print(r.status_code)




post_tweet(convert_quote(fetch_quote()))
