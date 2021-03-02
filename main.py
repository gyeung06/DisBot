from SocialLinkerClass import SocialLinker

import logging
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

logging.basicConfig(level=logging.INFO)

TOKEN = ''

bot = commands.Bot(command_prefix='~')

twitch_linker = SocialLinker("twitch_link", "twitch.tv/")
twitter_linker = SocialLinker("twitter_link", "twitter.com/")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('I have no idea what you want')


@bot.command(
    help="Helps my creator test stuff and adjust storage cuz he's dumb",
    brief="Does Nothing"
)
async def aa(ctx):
    pass


@bot.command(
    help="Call this with your twitch link, or someone else's and the link will be"
         "associated with your account to call with ~mtwitch",
    brief="Associates your account with your twitch link\n"
)
async def itwitch(ctx, link):
    if twitch_linker.create_link(ctx, link):
        await ctx.send('Got it')
    else:
        await ctx.send('Not a twitch link')


@bot.command(
    help="When called with no mentions will bring up your own twitch link -- "
         "If used with a mention will use that users associated link instead if they have one",
    brief="Calls either your twitch link or whoever you mention\n"
)
async def mtwitch(ctx, members: commands.Greedy[discord.Member]):
    if len(members) == 0:
        name = ctx.author.id
    elif len(members) == 1:
        name = members[0].id
    else:
        await ctx.send('One name at a time pal')
        return

    link = twitch_linker.retrieve_link(ctx, name)
    if link is not None:
        await ctx.send(link)
    else:
        await ctx.send('Link not set yet')


@bot.command(
    help="Call this with your twitter link, or someone else's and the link will be"
         "associated with your account to call with ~mtwitter",
    brief="Associates your account with your twitter link\n"
)
async def itwitter(ctx, link):
    if twitter_linker.create_link(ctx, link):
        await ctx.send('Got it')
    else:
        await ctx.send('Not a twitch link')


@bot.command(
    help="When called with no mentions will bring up your own twitter link -- "
         "If used with a mention will use that users associated link instead if they have one",
    brief="Calls either your twitter link or whoever you mention\n"
)
async def mtwitter(ctx, members: commands.Greedy[discord.Member]):
    if len(members) == 0:
        name = ctx.author.id
    elif len(members) == 1:
        name = members[0].id
    else:
        await ctx.send('One name at a time pal')
        return

    link = twitter_linker.retrieve_link(ctx, name)
    if link is not None:
        await ctx.send(link)
    else:
        await ctx.send('Link not set yet')


@bot.command(
    help="Just do it",
    brief="Try it\n"
)
async def bestwep(ctx):
    await ctx.send('DEBATE CLUB')
    await ctx.send(file=discord.File('TrulyTheBest.png'))


bot.run(TOKEN)
