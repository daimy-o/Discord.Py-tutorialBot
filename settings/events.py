import discord  # Inportation de la bibliotèque discord !
from discord.ext import commands # Importation de la fonction commands de la bibliothèque discord !

bot = commands.Bot(command_prefix='&', intents=discord.Intents.all())

@bot.event # Nous allons utiliser un évènement 
async def on_message(message : discord.Message): # Ici, la librairie de discord.Py permet de convertir les paramètre en le type que l'on precis [discord.Message] dans notre cas !
    if "salut" in message.content and message.author.bot == False: # Ici on verifie aussi que l'auteur du message n'est pas le bot et que le mot "salut" est compris dans le message envoyé !
        await message.channel.send("Salut à toi aussi!") # Ici, l'on peut faire : await interaction.reply("message"), pour que le bot repondre en interaction à l'utilisateur !
    # Ici, await car pour appeller une fonction qui est asynchrone, il faut obligatoirement utiliser le mot clé "await" !

@bot.event
async def on_message_delete(message : discord.Message,):
    contenu = message.content
    auteur = message.author
    lieu = message.channel
    respo = "Inconu"
    embed = discord.Embed(
        title="Suppression de message",
        description="```{}```".format(contenu),
        color=discord.Color.blue()
    )

    embed.set_author(name="On message delete", icon_url="")
    embed.set_thumbnail(url=auteur.avatar.url)
    embed.add_field(name="Auteur", value="{}".format(auteur), inline=True)
    embed.add_field(name="Salon", value="{}".format(lieu), inline=True)
    embed.add_field(name="Responsable", value="{}".format(respo), inline=True)
    embed.set_footer(text="")

    await message.channel.send(embed=embed)



@bot.event # Ici, nous appelons la methode event pour nous en servir comme decorateur (#RECHERCHEz)
async def on_ready(): # "async" represente une fonction asyncrome car si par exemple plusieur utilisateur appellent des cmds en même temps faudrait pas que chaque utilisateur ai à attendre son tour avant d'avoir une reponse !
    print("The bot is Only !")

__all__ = ['on_message', 'on_ready', 'on_message_delete']
# Les events qui seront pris en charge dans le main !