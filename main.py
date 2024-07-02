import discord
from discord.ext import commands

# Initialize the bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Bot token
TOKEN = 'token'


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.attachments:
        for attachment in message.attachments:
            if attachment.url.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp')):
                # React with upvote and downvote emojis
                await message.add_reaction('👍')  # Upvote emoji
                await message.add_reaction('👎')  # Downvote emoji
                break

# Run the bot

bot.run(TOKEN)
