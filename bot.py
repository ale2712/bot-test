import json
import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

client = commands.Bot(command_prefix="$")
status = cycle(["Ciao, io sono Kappa-bot", "scrivi $info per iniziare"])

@client.event
async def on_ready():
    change_status.start()
    print("Sono online", client.user)

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_message(message):
    channel = message.channel
    author = message.author
    authorid = message.author.id
    
    await client.process_commands(message)

    message.content.lower()
    if message.author == client.user:
        return

@client.command()
async def info(ctx):

    embed = discord.Embed(
        colours=discord.Colour.blue(),
        title="info",
        description="Ecco tutte le info sul server e sul bot"
    )

    embed.set_thumbnail(url="https://media.discordapp.net/attachments/703587414991437854/709350027876761640/690864056760008774.gif")
    embed.add_field(name="founder", value="Il founder di questo server è Gigli#7559")
    embed.add_field(name="developer", value="Il developer di questo bot è ale27_12#7151, per qualsiasi problema con il bot contattalo")
    embed.set_footer(text="Usa $commands per vedere i comandi")

    await ctx.send(embed=embed)

@client.command()
async def jojo(ctx):

    embed = discord.Embed(
        colours=discord.Colour.blue(),
        title="jojo reference",
        description="IS THIS A JOJO REFERENCE?"
    )

    embed.set_thumbnail(url="https://discordemoji.com/assets/emoji/7526_single_jojo_sign.png")

    await ctx.send(embed=embed)

@client.command()

async def commands(ctx):

    embed = discord.Embed(
        colours=discord.Colour.blue(),
        title="Comandi",
        description="Qui ci sono tutti i comandi di Kappa-bot"
    )

    embed.add_field(name="$jojo", value="Beh, questo comando non ha bisogno spiegazioni")
    embed.add_field(name="$info", value="In questo comando troverai le info sul founder di Kappa-comunity e sul developer di questo bot")
    embed.add_field(name="$youtube", value="Manda il link del canale youtube di Gigli")
    embed.set_footer(text="Fine sezione comandi")

    await ctx.send(embed=embed)

@client.command()

async def youtube(ctx):
    
    embed = discord.Embed(
        colours=discord.Colour.blue(),
        title="Youtube",
        description="Ecco il canale youtube di Gigli"
    )

    embed.add_field(name="link", value="https://www.youtube.com/channel/UC3Pb69lqB9PrXg0LqxCwXbQ")

    await ctx.send(embed=embed)

client.run("NzA5NzYyMjQyMjI0MTkzNTk2.XudwYQ.xa1Ix3-pU25uhugiWJ1jyYhP4hA")