from art import text2art
from nextcord.ext import commands
import nextcord

intents = nextcord.Intents.all()


class Bot(commands.Bot):

    async def register_bulk_application_commands(self) -> None:
        pass

    async def on_ready(self):
        print("Ready")
        for m in self.guilds[0].members:
            if str(m.status) == "online" and not m.bot:
                print(m)


channel = 917830355883524168

b = Bot(command_prefix=".", intents=intents)


@b.event
async def on_presence_update(before: nextcord.Member, after):
    if str(before.status) == "offline" and str(after.status) == "online":
        if before.id == 361503795269599234:
            await b.get_channel(channel).purge(limit=100)
            await b.get_channel(channel).send(f"Hello <@{after.id}>. Nothing happend here, I promise! ;-)")
        else:
            await b.get_channel(channel).send(f"Hello <@{after.id}>")


@b.command()
async def cat(ctx):
    """Prints a cat"""
    with open("cat", "r") as f:
        await ctx.send(f"```\n{f.read()}\n```")


@b.command()
async def moebius(ctx):
    """Prints a moebius triangle"""
    with open("moebius", "r") as f:
        await ctx.send(f"```\n{f.read()}\n```")


@b.command()
async def telescope(ctx):
    """Prints a radio telescope"""
    with open("telescope", "r") as f:
        await ctx.send(f"```\n{f.read()}\n```")


@b.command()
async def ascii(ctx, *, text=None):
    if text is None:
        await ctx.send("You must specify a text")
    await ctx.send(f"```\n{text2art(text)}\n```")


@b.command()
async def clear(ctx):
    await ctx.channel.purge(limit=100)

b.run("")
