# coding: UTF-8
import discord
import asyncio
import os
import re
from sub_package import getcardname, getxml, getprice

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    result_message = ""

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if re.match("^/howmuch",message.content):
        cardname = getcardname.func_getcardname(message.content)
        if cardname == "error":
            result_message = "指定されたカード名は見つかりませんでした。"
        else :
            url = getxml.func_getxml(cardname)
            result_message = getprice.func_getprice(url,cardname)



        await message.channel.send(result_message)


client.run("INSERT_YOUR_DISCORD_KEY")
