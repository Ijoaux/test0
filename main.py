import discord
import random
import asyncio
#________________OTHER FUNGSI
from title1 import pass_gen
from discord.ext import commands

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
intents.members = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

#bot = commands.Bot(command_prefix='!', intents=intents)
#____________________GUESSING GAME



class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long it was {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send(f'Oops. It is actually {answer}.')
   
            
        if message.content.startswith('$hello'):
            await message.reply("Hi!", mention_author=True)

        elif message.content.startswith('$bye'):
            await message.channel.send("😀")

        elif message.content.startswith('$Trade'):
            await message.channel.send("Succesfully DENIED")

        elif message.content.startswith('$random pass'):
            await message.channel.send(pass_gen(10))

        if message.content.startswith('$help'):
            await message.channel.send("$hello, $bye, $Trade, $random pass, $guess")


client = MyClient(intents=intents)

client.run(".")

#__________________BOTBOTBOT
#@bot.event
#async def on_ready():
    #print(f'We have logged in as {bot.user}')

#@bot.command()
#async def hello(ctx):
    #await ctx.send(f'Hi! I am a bot {bot.user}!')

#@bot.command()
#async def heh(ctx, count_heh = 5):
    #await ctx.send("he" * count_heh)

#@bot.command()
#async def password(ctx, f = 10):
    #await ctx.send(pass_gen(f))

#bot.run(".")
#_______________________bot bot bot______________

 #@client.event
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

    

#client.run(".")


