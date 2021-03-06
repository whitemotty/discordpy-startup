from discord.ext import commands
import discord
import os
import traceback
import random
import gundictionary as gun

bot = commands.Bot(command_prefix='*',activity=discord.Game("マックのバイト"),help_command=None)
bot.remove_command("help")
token = os.environ['DISCORD_BOT_TOKEN']

food_path = "./foods"
food_files = os.listdir(food_path)

fuze_path = "./fuze"

con = ['*help','*job','*today']
can = ['すまねぇ、今日は先約有りや…','すまねぇ、今日は遊べないや','今日オープンクローズだから無理や…']
ser = ['いきたみ','呼んだ？','ライトアモある？','全部俺の','スト5やろうかな…','エペやりたみががが','ぎるぎあはもういっかなぁ…']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_message(message):
    print(message.content)
    if message.author.bot:
        return
    if message.content.startswith('*help'):
        await bot.process_commands(message)
        return
    if message.content in gun.dic:
        await message.channel.send(embed=gun.dic[message.content])
        return
    if message.content.startswith('<@345945099303256065>') or message.content.startswith('<@!345945099303256065>'):
        if random.randrange(10) < 5:
            fuze_img = fuze_path + "/fuze.png"
            await message.channel.send(content='もりちゃんだよ',file=discord.File(fuze_img))
            return
        elif random.randrange(10) < 9:
            fuze_img = fuze_path + "/gul.png"
            await message.channel.send(content='逆もりちゃんだよ',file=discord.File(fuze_img))
            return
        else:
            fuze_img = fuze_path + "/morizo.png"
            await message.channel.send(content='偽もりちゃんだよ',file=discord.File(fuze_img))
            return
    if random.randrange(10) < 2:
        if message.content.startswith('💩') or message.content.startswith(':poop:'):
            await message.channel.send(':poop:')
            return
        if message.content.startswith('<@775343042567340053>') or message.content.startswith('<@!775343042567340053>') or message.content.startswith('<@&775398756547690516>'):
            await message.channel.send('草')
            return
        if message.content.startswith('<@337590899775242240>') or message.content.startswith('<@!337590899775242240>'):
            await message.channel.send(random.choice(can))
            return
        if 'ゆーし' in message.content:
            await message.channel.send('呼んだ？')
            return
        if '飯' in message.content:
            food_img = food_path + "/" + random.choice(food_files)
            await message.channel.send(content='今日の俺のごはんこれだよ',file=discord.File(food_img))
            return
        if message.content not in con and random.randrange(10) < 1:
            await message.channel.send(random.choice(ser))
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

@bot.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == 644381235753385985 and (before.channel != after.channel):
        alert_channel = bot.get_channel(644381236424343552)
        if before.channel is None and len(after.channel.members) == 1:
            embed = discord.Embed(title="通話開始", description="通話が開始されました．俺はバイトあるから行けないや．", color=0x66cdaa)
            embed.add_field(name="`ボイスチャンネル`", value=after.channel.name, inline=True)
            embed.add_field(name="`開始者`", value=member.name, inline=True)
            await alert_channel.send(embed=embed)

bot.run(token)
