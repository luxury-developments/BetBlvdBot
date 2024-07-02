import discord
import os

# Initialize the bot client
client = discord.Client()

# Event: Bot is ready
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Event: Message received
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Run the bot with your token from environment variables
client.run(os.getenv('MTI1NzQzNjYyODY4MzcxODc2Ng.G5ozXl.h5JYN8iguhcH_WrdIr4lYM_g0nWVKoP-szlbTU'))
