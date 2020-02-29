import discord
from discord.ext import commands

import logging

logger = logging.getLogger("Modmail")


class RemoveSelfStars(commands.Cog):
    """Removes self-stars for starboard."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        server = self.bot.get_guild(payload.guild_id)
        member = server.get_member(payload.user_id)
        try:
            message = await member.fetch_message(payload.message_id)
            if payload.emoji == "⭐" and payload.user_id == message.author.id:
                try:
                    await message.remove_reaction(payload.member, "⭐")
                except discord.Forbidden:
                    logger.error(
                        f"I didn't have permissions to remove a self star from {payload.member.name}#{payload.member.discriminator}."
                    )
                except Exception as e:
                    logger.error(e)
        except discord.NotFound:
            pass


def setup(bot):
    bot.add_cog(RemoveSelfStars(bot))
