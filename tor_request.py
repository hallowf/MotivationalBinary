import socks
import socket
import requests

socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket

def tor_fetch_quote():
    parsed_response = req.json()
    contents_obj = parsed_response["contents"]
    quotes_obj = contents_obj["quotes"][0]
    quote = quotes_obj["quote"]
    return quote
