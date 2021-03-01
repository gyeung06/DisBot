import logging
import json
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound


logging.basicConfig(level=logging.INFO)

TOKEN = ''

bot = commands.Bot(command_prefix='~')


def write_json(data, filename='test.json'):
    with open(filename, "w") as outfile:
        json.dump(data, outfile)


def get_new_id(uid):
    inp = {
        "id": uid,
        "link": "",
        "groups": ""
    }
    return inp


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('I have no idea what you want')


@bot.command(
    help="Call this with your twitch link, or someone else's not my issue really and the link will be"
         "associated with your account to call with ~mTwitch",
    brief="Associates your account with your twitch link\n"
)
async def itwitch(ctx, link):
    file_users = open("test.json")
    users = json.load(file_users)
    file_users.close()
    user_found = False

    if len(link) < 23:
        await ctx.send('Not a twitch link')
        return
    temp_link = link[0:22]
    if temp_link == "https://www.twitch.tv/":
        for keyval in users['members']:
            if str(ctx.author.id) == str(keyval['id']):
                keyval['link'] = link
                user_found = True
                break

        if not user_found:
            new_entry = get_new_id(ctx.author.id)
            new_entry['link'] = link
            users['members'].append(new_entry)

        write_json(users)
        await ctx.send('Got it')
    else:
        await ctx.send('Not a twitch link')


@bot.command(
    help="When called with no mentions will bring up your own twitch link -- "
         "If used with a mention will use that users associated link instead if they have one",
    brief="Calls either your twitch link or whoever you mention\n"
)
async def mtwitch(ctx, members: commands.Greedy[discord.Member]):
    print('hu')
    if len(members) == 0:
        name = ctx.author.id
    elif len(members) == 1:
        name = members[0].id
    else:
        await ctx.send('One name at a time pal')
        return

    file_users = open("test.json")
    users = json.load(file_users)
    file_users.close()

    for keyval in users['members']:
        if str(name) == str(keyval['id']):
            if len(keyval['link']) < 23:
                await ctx.send('Link not set yet')
            else:
                await ctx.send(keyval['link'])
                return

    await ctx.send('Link not set yet')


@bot.command(
    help="Just do it",
    brief="Try it\n"
)
async def bestwep(ctx):
    await ctx.send('DEBATE CLUB')
    await ctx.send(file=discord.File('TrulyTheBest.png'))


bot.run(TOKEN)
