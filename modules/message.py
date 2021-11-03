import discord


def message(tittle=str, color=str("FF0000"), extra=str):
    color = int(color, base=16)
    embed = discord.Embed(
        title=tittle,
        color=color,
        description=extra
    )
    return embed
