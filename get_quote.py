import requests
import json
import codecs
import time


# Chuck api url
chuck_api = "https://api.chucknorris.io/jokes/random"


# Fetches a random quote from Chuck API
def fetch_random():
    # Make a request to Chuck api
    req = requests.get(chuck_api)
    # Parse to Json
    parsed_response = req.json()
    # Fetch only the quote
    quote = parsed_response["value"]
    # Return it
    return quote

# Convert the quote to HEX
def convert_quote(text):
    # Encode the text
    quote_encode = text.encode()
    # Encode to HEX
    hex_quote = codecs.encode(quote_encode, "hex")
    # Decode to String
    decode_hex = hex_quote.decode("utf8")
    # Find Length
    print(len(decode_hex))
    # If length > than 260 try again
    if (len(decode_hex) > 260):
        # Timeout to avoid too many requests
        time.sleep(60)
        # Fetch another quote and try to convert it again
        convert_quote(fetch_random())
    else:
        # Return the quote converted to HEX
        return decode_hex




print(convert_quote(fetch_random()))
