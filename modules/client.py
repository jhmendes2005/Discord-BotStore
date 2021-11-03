import discord
import json


with open("./config.exemplo.json") as f:
    config = json.load(f)
    token = config['token']
    command_Prefix = config['prefixCommand']

intents = discord.Intents.all()
intents.members = True
client = discord.Client(command_prefix=f"{command_Prefix}", intents=intents)
