import discord
from discord.ext import commands
from random import randint

bot = commands.Bot(command_prefix="", description="Mi primer bot para el dc de MCF. Esta va pa los MCF :heart:")

@bot.command()
async def MettatonInfo(ctx):
    yop=discord.Embed(title="Mi primer Bot para el Discord de MCF.\nEsta va pa los MCF :heart::alien::heart:")
    yop.add_field(name="Bot creado por:", value="@Gurin#2290")
    yop.set_thumbnail(url="https://vignette.wikia.nocookie.net/undertale/images/8/8a/MttTalk.gif/revision/latest?cb=20160114022813&path-prefix=es")
    await ctx.send(embed=yop)
    mettaton=(" \n**¡¡¡¡¡          OPCIONES          DISPONIBLES          !!!!!:**\n\n\n-->      SUMAR      NÚMEROS:\n`suma`      *(número)*      `mas/y/+/con`       *(otro número)*\n\n\n-->      RESTAR      NÚMEROS:\n`resta`      *(número)*      `menos/y/-/con`      *(otro número)*\n\n\n")
    mettaton+=("-->      EMOJIS      RANDOM      DE      MCF:\n`RandoMCF` ||*~~(escríbanlo bien plss)~~*||\n\n\n")
    mettaton+=("**¡              Y          MUCHO          MÁS              !**\n||*(o por lo menos espero que en algún futuro no muy lejano)*||\n               ***IT'S               SHOWTIME!***          ")
    await ctx.send(mettaton)
    await ctx.send("\n\nhttps://tenor.com/view/undertale-mettaton-gif-13292650")

@bot.command()
async def suma(ctx, num1:int, conector:str, num2:int):
    if (conector!="y") and (conector!="con") and (conector!="+") and (conector!="mas"):
        await ctx.send("Ooh Baby, hay un error en tu último mensaje. Por favor, inténtalo nuevamente.")
    else:
        await ctx.send(num1+num2)


@bot.command()
async def resta(ctx, num1:int, conector:str, num2:int):
    if (conector!="y") and (conector!="con") and (conector!="-") and (conector!="menos"):
        await ctx.send("Ooh Baby, hay un error en tu último mensaje. Por favor, inténtalo nuevamente.")
    else:
        await ctx.send(num1-num2)

emojis=["<:Koopa:230499543479877642>", "<:PedroSwag:230500539308310529>", "<:Reimu6:230501222837256203>", "<:donfrancis:230501645912375296>", "<:daniloenojado:230502662188171267>", "<:DIO:230503151617179648>", "<:Shrek:230504138792894464>"] 
emojis+=["<:danilo:230504159181275136>", "<:elmedel:230505300854046720>", "<:ituxd:596950697409380372>", "<:yoshi:664271315418611722>"]
emojis+=["<:silencio_minoria:719377433157173289>", "<:otis2:719377876633518140>", "<:freddypog:719378639283552307>", "<:yes:719379443558252564>", "<:otis:719381184504791080>", "<:ah_ya:722117047772905655>", "<:tom:733138011373437030>", "<:adios:733138584609226753>"] 
emojis+=["<:delet_this:733140318073126962>", "<:muplop:733140393083797565>", "<:kronks:733140520506884117>", "<:flaco:733141245316038727>", "<:tuve_fe:733141455568240720>", "<:arsene:733142472330313758>", "<:joya:733143391365496842>"]
largo = len(emojis)

@bot.command()
async def RandoMCF(ctx):
    ran=randint(0,largo-1)
    emoji=emojis[ran]
    await ctx.send(emoji)

@bot.event
async def on_ready():
    print("Tamos")

bot.run("") #se debe introducir el token

