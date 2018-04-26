import requests
import json
import codecs
import time

chuck_api = "https://api.chucknorris.io/jokes/random"



def fetch_random():
    req = requests.get(chuck_api)
    parsed_response = req.json()
    quote = parsed_response["value"]
    return quote


def convert_quote(text):
    quote_encode = text.encode()
    hex_quote = codecs.encode(quote_encode, "hex")
    decode_hex = hex_quote.decode("utf8")
    print(len(decode_hex))
    if (len(decode_hex) > 260):
        time.sleep(60)
        convert_quote(fetch_random())
    else:
        return decode_hex




print(convert_quote(fetch_random()))
