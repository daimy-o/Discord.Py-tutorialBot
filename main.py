import discord  # Inportation de la bibliotèque discord !
from discord.ext import commands # Importation de la fonction commands de la bibliothèque discord !
import config # Inportation de la config
import settings.commands # Importation du module commands dans le dossier settings !
import settings.events # Importation du module event dans le dossier settings !

bot = commands.Bot(command_prefix='&', intents=discord.Intents.all())
# Ici, nous avons defini les itents et le prefix de notre bot (et on a notre bot qui se nomme bot (ligne 6:1))
# Si par exemple on a "client = commands..." alors on aura : @client.event à la linge 9 !
 
 # Ajout des commandes du fichier command.py à notre bot
for command in settings.commands.__all__:
    bot.add_command(getattr(settings.commands, command))

# Ajout des eventes du fichier command.py à notre bot
for event in settings.events.__all__:
    bot.add_listener(getattr(settings.events, event))

bot.run(config.token)
# Lancement du bot !