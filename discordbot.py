from discord.ext import commands
import discord
import os
import traceback
import random

bot = commands.Bot(command_prefix='*',activity=discord.Game("マックのバイト"),help_command=None)
bot.remove_command("help")
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_message(message):
    print(message.content)
    if random.randrange(10) < 2:
        if message.author.bot:
            return
        if message.content.startswith('💩') or message.content.startswith(':poop:'):
            await message.channel.send(':poop:')
            return
        if message.content.startswith('<@!775343042567340053>'):
            await message.channel.send('草')
            return
        if message.content.startswith('<@!337590899775242240>'):
            await message.channel.send('すまねぇ、今日は先約有りや…')
            return
        if message.content not in ['*help','*job','*today']:
            await message.channel.send('呼んだ？')
            return
        await bot.process_commands(message)
    return
    
@bot.command()
async def job(ctx):
    await ctx.send('今日はオープンクローズかな')

@bot.command()
async def today(ctx):
    await ctx.send('すまねぇ、今日は遊べないや')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="ゆーしbot help", description="A Very Nice ゆーしbot.\nゆーし always works at McDonald's.\nThere's a 20% chance to reply.", color=0xeee657)

    embed.add_field(name="mention to ゆーしbot", value="笑われます", inline=False)
    embed.add_field(name="mention to オープンクローズ", value="ゆーしの代わりに返信します", inline=False)
    
    embed.add_field(name="*help", value="コマンド一覧の表示をします", inline=False)
    embed.add_field(name="*job", value="今日のバイトのシフトを伝えます", inline=False)
    embed.add_field(name="*today", value="今日の予定を伝えます", inline=False)

    await ctx.send(embed=embed)

bot.run(token)
