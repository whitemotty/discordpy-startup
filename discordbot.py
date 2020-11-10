#from discord.ext import commands
import discord
import os
import traceback

client = discord.Client(activity=discord.Game("マックのバイト"))
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    pass

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if client.user in message.mentions:
        await message.channel.send('草')
    if '<@!337590899775242240>' in message.content:
        await message.channel.send('すまねぇ、今日は先約有りや…')
    if message.content.startswith('*job')
        await message.channel.send('今日はオープンクローズかな')
    if message.content.startswith('*today')
        await message.channel.send('すまねぇ、今日は遊べないや')
    if message.content.startswith('*help')
        embed = discord.Embed(title="ゆーしbot help", description="A Very Nice ゆーしbot. List of commands are:", color=0xeee657)
        embed.add_field(name="mention to ゆーしbot", value="笑われます", inline=False)
        embed.add_field(name="mention to オープンクローズ", value="ゆーしの代わりに返信します", inline=False)
        embed.add_field(name="*help", value="コマンド一覧の表示をします", inline=False)
        embed.add_field(name="*job", value="今日のバイトのシフトを伝えます", inline=False)
        embed.add_field(name="*today", value="今日の予定を伝えます", inline=False)
        await message.channel.send(embed=embed)

client.run(token)
