import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='.', intents = discord.Intents.all())

@bot.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick_member(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.display_name} potkittiin palvelimelta. Syy: {reason}')

@bot.command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban_member(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.display_name} bännättiin palvelimelta. Syy: {reason}')


@bot.event
async def on_ready():
    print(f'{bot.user.name} ready to use.')

@bot.command(name='clear')
@commands.has_permissions(manage_messages=True)

@bot.command(name='juusto')
async def test(ctx):
    await ctx.send("Testikomento toimii!")
    
@bot.command()
async def Sano(ctx, *, viesti):
    await ctx.send(viesti)

    
bot.run('MTIwMzA1ODc0MTQ0OTMzMDc3OQ.G5ZAho.pDS9dKvJuRGSBzfhDoALkbDoxY44rUiH2EaCew')