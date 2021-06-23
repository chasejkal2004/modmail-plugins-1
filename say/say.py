import discord
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def addrole(ctx):
        thread = ctx.thread
        member = thread.recipient
        role = get(member.server.roles, name="Member")
        await ctx.add_roles(member, role)
def setup(bot):
    bot.add_cog(Say(bot))
