import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())


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
async def clear(ctx, amount: int):
    if amount <= 0 or amount > 100:
        await ctx.send('Anna määrä välillä 1-100.')
        return
    deleted = await ctx.message.channel.purge(limit=amount + 1)
    await ctx.send(f'Poistettiin {len(deleted) - 1} viestiä.')
    
bot.run('MTIwMzA1ODc0MTQ0OTMzMDc3OQ.G5ZAho.pDS9dKvJuRGSBzfhDoALkbDoxY44rUiH2EaCew')