# welcomeBot
# -*- coding: utf-8 -*-

import discord

# 初期設定など
TOKEN = 'NjA4Mjk2ODAxOTc5ODU4OTQ0.XUmJYQ.YnRJJUzS30ZDDfExHiexGRd_GTc'
TC_welcome = '<#608262414810742791>' # 新人さん用
TC_contact = '<#608303827472351234>' # 役職変更用
CLASS = "やっくしょっく" # 初期の役職を付与しちゃう

client = discord.Client()
welcome_chat = discord.Object(id=TC_welcome)
position_chat = discord.Object(id=TC_contact)

# 実行場所とか色々環境変化するのに対応できないため無理やり突っ込む
welcome_text  = "初めまして USER さん!\n"
welcome_text += "カンラン卓のサーバへようこそ！\n\n"
welcome_text += "セッションの募集や参加については_#セッション用の『<#608295461727502357>』\n"
welcome_text += "初めての挨拶や初雑談は全て『<#608295502185758743>』で！\n"
welcome_text += "何か VC 歓談所 が賑やかなときとかは『<#608295533852885023>』に Let's GO!!\n"
welcome_text += "サーバのルールや仕様については『<#608295623539687427>』\n"
welcome_text += "各ハウスルールについては『<#608295678354915339>』\n"
welcome_text += "他にも何か色々あるけど、詳しいことは『<#608295721606578176>』で確認を！\n\n"
welcome_text += "とりあえず、『みんななかよくプレイしましょう！』\n\n"
welcome_text += "さぁ、まずは<#608295502185758743>で交流を深めよう！"

# 起動したときにするやつ
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('カンラン亭の案内人, ログインしました.')

# 新人さんが来た時やるやつ
@client.event
async def on_member_join(member):
    # 挨拶と説明
    channel = member.guild.system_channel
    embed = discord.Embed(title="", description=welcome_text.replace('USER', member.mention), color=0xeee657)
    await channel.send(embed=embed)

# 動作テスト
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '/test':
        await message.channel.send(608274014477090827,'マイクのテスト中')


client.run(TOKEN)