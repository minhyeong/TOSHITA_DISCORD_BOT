
import discord

# TOKEN
TOKEN = 'NjA4MjYzODY3NTQ1NTUwODY4.XUlwMQ.rUEWxkXp7bEQ5iZDwpYwyOyfAg8'

client = discord.Client()

@client.event
async def on_message(message):
    # ボットの発言を無視
    if message.author.bot:
        return
    if message.content == 'test':
        await message.channel.send('テスト')

client.run(TOKEN)