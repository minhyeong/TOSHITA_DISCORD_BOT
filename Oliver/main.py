
# -*- coding: utf-8 -*-

import constant as c
import class_ as cl
import discord
import os

client = discord.Client()

FILE_NAME = os.path.abspath('sozai/welcomeText.txt')

@client.event
async def on_ready(): 
    # ログイン通知
    print('Oliver 起動しました')

@client.event
async def on_member_join(member):
    # 挨拶と説明
    channel = member.guild.system_channel
    text = cl.WelcomeText()
    embed = discord.Embed(title="", description = text.get_text(FILE_NAME).replace('#USER', member.mention), color=0xeee657)
    await channel.send(embed=embed)

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # ログアウトさせるコマンド
    if message.content == '/Oliver_Fin':
        await message.channel.send('Oliver ログアウトします')
        await client.logout()
        print('Oliver ログアウトしました')


client.run(c.TOKEN)