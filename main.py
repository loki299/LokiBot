import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix = commands.when_mentioned_or('-'))

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'AIUDA',
        description = '''
        Prefijo: -

        Comandos:
        - suma
        - resta
        - mult
        - div
        - avatar
        - pene
        - ping
        - cami
        - frio
        - spam (mensaje)
        - ban
        ''',
        color = discord.Color.gold()
    )
    await ctx.send(embed = embed)






@bot.command()
async def suma(ctx, a, b):
    embed = discord.Embed(
        title = 'Suma',
        description = f'El resultado es {int(a) + int(b)}',
        color = discord.Color.blurple()
    )
    await ctx.send(embed = embed)

@bot.command()
async def resta(ctx, a, b):
    embed = discord.Embed(
        title = 'Resta',
        description = f'El resultado es {int(a) - int(b)}',
        color = discord.Color.blurple()
    )
    await ctx.send(embed = embed)

@bot.command()
async def mult(ctx, a, b):
    embed = discord.Embed(
        title = 'Multiplicación',
        description = f'El resultado es {int(a) * int(b)}',
        color = discord.Color.blurple()
    )
    await ctx.send(embed = embed)

@bot.command()
async def div(ctx, a, b):
    embed = discord.Embed(
        title = 'División',
        description = f'El resultado es {int(a) / int(b)}',
        color = discord.Color.blurple()
    )
    await ctx.send(embed = embed)

@bot.command()
async def avatar(ctx, member:discord.Member = None):
    if member == None:
        user = discord.client.User
        await ctx.send(user.avatar_url)
    else:
        await ctx.send(member.avatar_url)

@bot.command()
async def miavatar(ctx):
    user = discord.Message.author
    await ctx.send(user.avatar_url)

@bot.command()
async def pene(ctx):
    await ctx.send('chupas')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency, 1)}ms')

@bot.command()
async def cami(ctx):
    await ctx.send('pasa fotos de nala porfis')

@bot.command()
async def frio(ctx):
    await ctx.send('cayate')

@bot.command()
async def spam(ctx, text):
    contador = 1
    while contador < 4:
        contador += 1
        await ctx.send(text)

@bot.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

bot.run(TOKEN)
