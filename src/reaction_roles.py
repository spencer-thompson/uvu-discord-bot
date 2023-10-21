import discord
from dotenv import load_dotenv
import os

load_dotenv()

# intents = discord.Intents.default()
# intents.message_content = True

# client = discord.Client(intents=intents)


class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 1165417626806267986 # In bot-testing channel

    async def on_ready(self):
        print('Client now Online')

    # wow async cool
    async def on_raw_reaction_add(self, payload):
        """
        Give a role based on reaction emoji
        """

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)

        if payload.emoji.name == '🎮':
            role = discord.utils.get(guild.roles, name='Gamer')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='Chocolate ;)')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🐒':
            role = discord.utils.get(guild.roles, name='monkey')
            await payload.member.add_roles(role)


    async def on_raw_reaction_remove(self, payload):
        """
        Remove a role b ased on a reaction emoji
        """

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '🎮':
            role = discord.utils.get(guild.roles, name='Gamer')
            await member.remove_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='Chocolate ;)')
            await member.remove_roles(role)
        elif payload.emoji.name == '🐒':
            role = discord.utils.get(guild.roles, name='monkey')
            await member.remove_roles(role)

# Only runs if this is the entrypoint
if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.members = True

    client = MyClient(intents=intents)
    client.run(os.getenv('bot_token'))