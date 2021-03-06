from turtle import color
from urllib import response
import discord
from discord.ext import commands
import requests, json
from youtube_dl import YoutubeDL
import time
import asyncio
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
from http import client
from idna import valid_contextj
import discord, datetime, asyncio, random
import datetime
import discord, asyncio, datetime, pytz
from discord.ext.commands import bot
from discord import Embed

bot = commands.Bot(command_prefix='!')

client = discord.Client()

user = []
musictitle = []
song_queue = []
musicnow = [] 

def title(msg):
    global music

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    chromedriver_dir = r"C:\Users\sec\Downloads\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver_dir, options = options)
    driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
    source = driver.page_source
    bs = bs4.BeautifulSoup(source, 'lxml')
    entire = bs.find_all('a', {'id': 'video-title'})
    entireNum = entire[0]
    music = entireNum.text.strip()
    
    musictitle.append(music)
    musicnow.append(music)
    test1 = entireNum.get('href')
    url = 'https://www.youtube.com'+test1
    with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
    URL = info['formats'][0]['url']

    driver.quit()
    
    return music, URL

def play(ctx):
    global vc
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    URL = song_queue[0]
    del user[0]
    del musictitle[0]
    del song_queue[0]
    vc = get(bot.voice_clients, guild=ctx.guild)
    if not vc.is_playing():
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx)) 

def play_next(ctx):
    if len(musicnow) - len(user) >= 2:
        for i in range(len(musicnow) - len(user) - 1):
            del musicnow[0]
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if len(user) >= 1:
        if not vc.is_playing():
            del musicnow[0]
            URL = song_queue[0]
            del user[0]
            del musictitle[0]
            del song_queue[0]
            vc.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS), after=lambda e: play_next(ctx))

    else:
        if not vc.is_playing():
            client.loop.create_task(vc.disconnect())

@bot.event
async def on_ready():
    print('???????????? ??????????????????: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def ?????????(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("????????? ????????? ??????????????? ?????????..")

@bot.command()
async def ??????(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send("?????? ??? ????????? ???????????? ?????????.")

@bot.command()
async def ??????(ctx, *, url):
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("????????? ????????? ??????????????? ?????????..")

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "?????? ??????", description = "?????? " + url + "???(???) ???????????? ????????????.", color = 0x00ff00))
    else:
        await ctx.send("????????? ?????? ???????????? ????????????!")

@bot.command()
async def ????????????(ctx):
    if vc.is_playing():
        vc.pause()
        await ctx.send(embed = discord.Embed(title= "????????????", description = musicnow[0] + "???(???) ???????????? ????????????.", color = 0x00ff00))
    else:
        await ctx.send("?????? ????????? ???????????? ?????????.")

@bot.command()
async def ????????????(ctx):
    try:
        vc.resume()
    except:
         await ctx.send("?????? ????????? ???????????? ?????????.")
    else:
         await ctx.send(embed = discord.Embed(title= "????????????", description = musicnow[0]  + "???(???) ?????? ??????????????????.", color = 0x00ff00))

@bot.command()
async def ????????????(ctx):
    if vc.is_playing():
        vc.stop()
        await ctx.send(embed = discord.Embed(title= "????????????", description = musicnow[0]  + "???(???) ??????????????????.", color = 0x00ff00))
    else:
        await ctx.send("?????? ????????? ???????????? ?????????.")

@bot.command()
async def ????????????(ctx):
    if not vc.is_playing():
        
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        chromedriver_dir = r"C:\Users\sec\Downloads\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver_dir, options = options)
        driver.get("https://www.youtube.com/results?search_query=????????????")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "?????? ??????", description = "?????? " + musicnow[0] + "???(???) ???????????? ????????????.", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("?????? ????????? ?????? ????????? ????????? ????????? ??? ?????????!")

@bot.command()
async def ???????????????(ctx, *, msg):
    user.append(msg)
    result, URLTEST = title(msg)
    song_queue.append(URLTEST)
    await ctx.send(result + "??? ??????????????? ???????????????!")

@bot.command()
async def ???????????????(ctx, *, number):
    try:
        ex = len(musicnow) - len(user)
        del user[int(number) - 1]
        del musictitle[int(number) - 1]
        del song_queue[int(number)-1]
        del musicnow[int(number)-1+ex]
            
        await ctx.send("???????????? ??????????????? ?????????????????????.")
    except:
        if len(list) == 0:
            await ctx.send("???????????? ????????? ?????? ????????? ??? ?????????!")
        else:
            if len(list) < int(number):
                await ctx.send("????????? ????????? ??????????????? ??????????????????!")
            else:
                await ctx.send("????????? ??????????????????!")

@bot.command()
async def ??????(ctx):
    if len(musictitle) == 0:
        await ctx.send("?????? ??????????????? ???????????? ????????????.")
    else:
        global Text
        Text = ""
        for i in range(len(musictitle)):
            Text = Text + "\n" + str(i + 1) + ". " + str(musictitle[i])
            
        await ctx.send(embed = discord.Embed(title= "????????????", description = Text.strip(), color = 0x00ff00))

@bot.command()
async def ???????????????(ctx):
    try:
        ex = len(musicnow) - len(user)
        del user[:]
        del musictitle[:]
        del song_queue[:]
        while True:
            try:
                del musicnow[ex]
            except:
                break
        await ctx.send(embed = discord.Embed(title= "???????????????", description = """????????? ??????????????? ????????????????????????. ?????? ????????? ???????????????????""", color = 0x00ff00))
    except:
        await ctx.send("?????? ??????????????? ???????????? ????????????.")

@bot.command()
async def ????????????(ctx):

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("????????? ????????? ??????????????? ?????????..")

    if len(user) == 0:
        await ctx.send("?????? ??????????????? ???????????? ????????????.")
    else:
        if len(musicnow) - len(user) >= 1:
            for i in range(len(musicnow) - len(user)):
                del musicnow[0]
        if not vc.is_playing():
            play(ctx)
        else:
            await ctx.send("????????? ?????? ???????????? ?????????!")

@bot.command()
async def ?????????(ctx, seconds):
    try:
        secondint = int(seconds)
        if secondint > 3600:
            await ctx.send("3600?????? ????????? ?????????????????? ??? ??? ?????????")
            raise BaseException
        if secondint <= 0:
            await ctx.send("???????????? ????????? ?????? ???????????? ??????????????????")
            raise BaseException
        message = await ctx.send(f"?????????: {seconds}")
        while True:
            secondint -= 1
            if secondint == 0:
                await message.edit(content="????????? ???!")
                break
            await message.edit(content=f"?????????: {secondint}")
            await asyncio.sleep(1)
        await ctx.send(f"{ctx.author.mention} ???????????? ?????????????????????!")
    except ValueError:
        await ctx.send("????????? ??????????????????!!")

@bot.command()
async def ?????????(ctx, number: str):
    if ctx.author.guild_permissions.administrator:

        if int(number) > 21600 or int(number) <= 0:
            raise commands.BadArgument
        else:
            await ctx.channel.edit(slowmode_delay=int(number))
            embed1 = discord.Embed(title=f"?????? ????????? ????????? {number}?????? ??????????????????!",
                                   color=0xFF00DD)
            await ctx.reply(embed=embed1)
    else:
        embed2= discord.Embed(title="???????????? ????????? ??? ?????? ????????? ?????????!", color=0xFF0000)
        await ctx.send(embed=embed2)

@bot.command()
async def ????????????(ctx, *, msg):
    response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{msg}").json()
    uuid = response["id"]
    print(uuid)
    name_history = requests.get(f"https://api.mojang.com/user/profiles/{uuid}/names")
    namehis = json.loads(name_history.text)
    name = []
    for x in namehis:
        name.append(x["name"])
    image_small = f"https://visage.surgeplay.com/face/{uuid}"
    image_big = f"https://visage.surgeplay.com/bust/{uuid}"
    e = Embed(title=f"??????  **{msg}**?????? ?????????????????? ??????", color=0x00FFF)
    e.add_field(name="#??????  UUID:", value=f"**{uuid}**", inline=False)
    e.add_field(name="????  ?????? ?????? ??????:", value='**->**'.join(name), inline=False)
    e.set_thumbnail(url=image_small)
    e.set_image(url=image_big)
    await ctx.send(embed=e)

bot.run("OTQwNDE3ODYzNTk0OTYzMDE1.YgHGYg.x-jYBK1qK6UJ54pPKxflsDu6XSc")