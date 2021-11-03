import json
from utils import commands as Commands, messages as Messages

Listcommands = Commands.command
listMessage = Messages.messages
command_Prefix = str

with open("./config.exemplo.json") as f:
    config = json.load(f)
    command_Prefix = config['prefixCommand']


class validate:
    async def checkCommand(message):
        channel = message.channel
        content: str = message.content.lower()
        if(content.startswith(command_Prefix)):
            content = content.replace(command_Prefix, "")
            content = content.split()[0]
            if(hasattr(Listcommands, content) is True):
                command = getattr(Listcommands, content)
                await command(message)
            else:
                await channel.send("Command not found")

    async def checkMessage(message):
        channel = message.channel
        content: str = message.content.lower().replace(" ", "")

        if(hasattr(listMessage, content) is True):
            embed = getattr(listMessage, content)
            embed = embed()
            await channel.send(embed=embed)