import discord
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def addrole(ctx):
        thread = ctx.thread
        user = thread.recipient
        role = discord.utils.get(user.guild.roles, name="Trusted")
        await user.add_roles(role)
def setup(bot):
    bot.add_cog(Say(bot))
