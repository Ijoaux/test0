import discord
from title1 import pass_gen
from discord.ext import commands

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, f = 10):
    await ctx.send(pass_gen(f))

bot.run("IDK")


# @client.event
# async def on_ready():
#     print(f'Kita telah masuk sebagai {client.user}')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content.startswith('$halo'):
#         await message.channel.send("Hi!")
#     elif message.content.startswith('$bye'):
#         await message.channel.send("😀")
#     elif message.content.startswith('$Trade'):
#         await message.channel.send("Succesfully DENIED")
#     if message.content.startswith('$random pass'):
#         await message.channel.send(pass_gen(10))

#     else:
#         await message.channel.send(message.content)

    

#client.run("MTEyNDUxMDg0MTU0NzUyNjMwNw.Gpa0z4.WLDFlRrR5VRDS6VbXaphjOduRnguRSrYKou6fg")

