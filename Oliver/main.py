
# -*- coding: utf-8 -*-

import constant as c
import discord
import os

client = discord.Client()

FILE_NAME = os.path.abspath('Oliver/sozai/welcomeText.txt')

def convert_ID(original_text): # チャンネル名をＩＤに変更
    convert_text = original_text#.replace('', '')
    return convert_text

def get_text(file_name):
    f = open(file_name, 'r', encoding="utf-8_sig")
    line = f.readline()
    read_text = ''
    while line:
        line = f.readline()
        read_text += line
    f.close()
    #return convert_ID(read_text)
    return read_text 

@client.event
async def on_ready(): 
    # ログイン通知
    print('Oliver 起動しました')

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '/welcome_test':
        member = "<@308211485086056449>"
        #embed = discord.Embed(title="", description = get_text(FILE_NAME).replace('USER', member.mention), color=0xeee657) # こっちが運用側
        embed = discord.Embed(title=get_text(FILE_NAME).replace('USER', member), description = "", color=0xeee657)
        await message.channel.send(embed=embed)

client.run(c.TOKEN)