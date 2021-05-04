#!/usr/bin/python3
"""Making API requests with python"""

# this is 3rd party library (wildly popular)
# python3 -m pip install requests
import requests

API = "http://api.open-notify.org/astros.json"

def main():
    """runtime code"""
    astrosresp = requests.get(API)  # send an HTTP GET to our API

    astros = astrosresp.json() # this converts json attached to HTTP response to pythonic data (list / dict)

    print(astros.get("people"))

    print(astros.get("number"))

if __name__ == "__main__":
    main()
