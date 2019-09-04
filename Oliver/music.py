
# -*- coding: utf-8 -*-

import constant as c
import class_ as cl
import music as mp
import discord
import os

client = discord.Client()

youtube_url = 'https://www.youtube.com/watch?v=7z4WJAEG3u8'

@client.event
async def on_message(message):
    if message.author.bot:
        return

    voice = await client.connect()(client.get_channel(614344189286809612))
    if message.content == ("lecture"):
        player = await voice.create_ytdl_player(youtube_url)
        player.start()

    if message.content == ("bgm"):
        player = await voice.create_ytdl_player(youtube_url)
        player.start()

client.run(c.TOKEN)