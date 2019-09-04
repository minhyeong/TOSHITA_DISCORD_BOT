
# -*- coding: utf-8 -*-

import constant as c
import class_ as cl
#import music as mp
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
    # 新人さんにGESTタグの付与
    role = discord.utils.get(member.guild.roles, name='GUEST')
    await member.add_roles(role)

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # ログアウトさせるコマンド
    if message.content == '!SHUTDOWN_OLIVER':
        await message.channel.send('Oliver ログアウトします')
        print('Oliver ログアウトしました')
        await client.logout()

    # GUESTタグが付与される
    if message.content == '/join':
        role = discord.utils.get(message.guild.roles, name='GUEST')
        await message.author.add_roles(role)
    

client.run(c.TOKEN)