import discord 
from discord import app_commands
from freeai.skybyte.main import ask
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_APPLICATION = os.getenv("DISCORD_APPLICATION")
DISCORD_GUILD = discord.Object(id=os.getenv('DISCORD_GUILD'))



class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents, application_id: int):
        super().__init__(intents=intents, application_id=application_id)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=DISCORD_GUILD)
        await self.tree.sync(guild=DISCORD_GUILD)

intents = discord.Intents.all()
client = MyClient(intents=intents, application_id=DISCORD_APPLICATION)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}\nUser id: {client.user.id}")
    for guild in client.guilds:
        print(f"- {guild.name} ({guild.id}), {guild.member_count} members")





@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if "ai" in message.channel.name:
        await message.channel.send(ask(message.content))

client.run(DISCORD_TOKEN)


        
    


        
    

