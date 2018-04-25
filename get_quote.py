import requests
import json


quotes_url = "http://quotes.rest/qod.json"

def fetch_quote():
    req = requests.get(quotes_url)
    if req.status_code == 429:

    parsed_response = req.json()
    contents_obj = parsed_response["contents"]
    quotes_obj = contents_obj["quotes"][0]
    quote = quotes_obj["quote"]
    return quote



def convert_quote(text):
    bin_quote = ' '.join(map(bin,bytearray(text,'utf8')))
    bin_quote = bin_quote.replace("b", "")
    return bin_quote




print(convert_quote(fetch_quote()))
