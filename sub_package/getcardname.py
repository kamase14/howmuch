# coding: UTF-8
import discord
import asyncio
import requests
import time
import json

fuzzysearch_api = 'https://api.scryfall.com/cards/named?fuzzy={name}'

def func_getcardname(message) :
    cardname = message.replace("/howmuch","")
    cardname = cardname.replace(" ","")
    print(cardname)

    url = fuzzysearch_api.format(name=cardname)

    r = requests.get(url)
    data = json.loads(r.text)

    if data["object"] == "card":

        result = data["name"]

    elif data["object"] == "error":

        result = "error"

    time.sleep(0.1)

    return result
