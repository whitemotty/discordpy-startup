from discord.ext import commands
import discord
import os
import traceback

bot = commands.Bot(command_prefix='*',activity=discord.Game("マックのバイト"))
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if client.user in message.mentions:
        await message.channel.send('草')
    if '<@!337590899775242240>' in message.content:
        await message.channel.send('すまねぇ、今日は先約有りや…')
    #await bot.process_commands(message)

@bot.command()
async def job(ctx):
    await ctx.send('今日はオープンクローズかな')

@bot.command()
async def today(ctx):
    await ctx.send('すまねぇ、今日は遊べないや')

"""
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="ゆーしbot help", description="A Very Nice ゆーしbot. List of commands are:", color=0xeee657)

    embed.add_field(name="mention to ゆーしbot", value="笑われます", inline=False)
    embed.add_field(name="mention to オープンクローズ", value="ゆーしの代わりに返信します", inline=False)
    
    embed.add_field(name="*help", value="コマンド一覧の表示をします", inline=False)
    embed.add_field(name="*job", value="今日のバイトのシフトを伝えます", inline=False)
    embed.add_field(name="*today", value="今日の予定を伝えます", inline=False)

    await ctx.send(embed=embed)
"""

bot.run(token)
