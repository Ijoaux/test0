import discord
import random
import asyncio
import os
import requests

from discord.ext import commands
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def animal_meme(ctx):
    mlg_name = random.choice(os.listdir("newer"))
    with open(f'newer/{mlg_name}', 'rb') as f:
            picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


bot.run("-")


