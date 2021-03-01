import logging
import json
from discord.ext import commands
from discord.ext.commands import CommandNotFound


logging.basicConfig(level=logging.INFO)

TOKEN = ''

bot = commands.Bot(command_prefix='~')


def write_json(data, filename='test.json'):
    with open(filename, "w") as outfile:
        json.dump(data, outfile)


def get_new_id(id):
    inp = {
        "id": id,
        "link": "",
        "groups": ""
    }
    return inp


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('I have no idea what you want')



@bot.command()
async def iTwitch(ctx, link):
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

        if not user_found:
            new_entry = get_new_id(ctx.author.id)
            new_entry['link'] = link
            users['members'].append(new_entry)

        write_json(users)
        await ctx.send('I got you homie')
    else:
        await ctx.send('Not a twitch link')


@bot.command()
async def mTwitch(ctx):



@bot.command()
async def bestWep(ctx):
    await ctx.send('DEBATE CLUB')


bot.run(TOKEN)
