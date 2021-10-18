import discord
from discord import channel
from discord.ext import commands
from discord.flags import Intents
import json
import random
import os

with open("Sarii_Bot_setting.json", "r", encoding = "UTF-8") as f:      #開啟.json "r"(讀) 
    jData = json.load(f)

Intents = discord.Intents.all()     #所有權限

bot = commands.Bot(command_prefix= ".", Intents = Intents)      #指令用"."開頭


@bot.event
async def on_ready():       #當機器人啟動時
    print(">> Link Start <<")
    channel = bot.get_channel(int(jData["WELCOME"]))        #在"WELCOME"頻道
    await channel.send(">>      Link Start      リンクスタート！<<")    #輸出這句話
    random_link_start = random.choice(jData["URL_LINK_START"])      #從"URL_LINK_START中隨機選一個gif連結
    await channel.send(random_link_start)       #輸出連結
    status_w = discord.Status.online        #設定機器人狀態 (上線)
    activity_w = discord.Activity(type=discord.ActivityType.watching, name="你的可撥人生", url = "https://youtu.be/dQw4w9WgXcQ")    #type(觀看中) 底下的文字(你的可撥人生)
    await bot.change_presence(status= status_w, activity=activity_w)    #設定狀態



@bot.command()
async def lo(ctx, extension):
    bot.load_extension(f"bot_cmds.{extension}")
    await ctx.send(f"載入{extension}完成")

@bot.command()
async def un(ctx, extension):
    bot.unload_extension(f"bot_cmds.{extension}")
    await ctx.send(f"解除載入{extension}完成")

@bot.command()
async def re(ctx, extension):
    bot.reload_extension(f"bot_cmds.{extension}")
    await ctx.send(f"重新載入{extension}完成")


for Filename in os.listdir("./bot_cmds"):
    if Filename.endswith(".py"):
        bot.load_extension(f"bot_cmds.{Filename[:-3]}")

if __name__ == "__main__":
    bot.run(jData["TOKEN"])