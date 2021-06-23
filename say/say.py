import discord
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def say2(self, ctx, *, message):
        """ModMail says what you want it to say."""
        await ctx.send(message.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere"))
        await ctx.message.delete()


    @commands.command(pass_context=True)
    async def addrole(ctx):
        thread = ctx.thread
        member = thread.recipient
        role = get(member.server.roles, name="Member")
        await comamnds.add_roles(member, role)
def setup(bot):
    bot.add_cog(Say(bot))
