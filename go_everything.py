import discord
from discord.ext import commands
import discord_config
import midjourney as mj
import discord_util as dut
import time

client = commands.Bot(command_prefix='*', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot connected')

@client.event
async def on_message(message):
    msg_content = message.content
    # print(message)

    for attachment in message.attachments:
        print(f'** Attachment found : message: {message.id}')
        file_prefix = time.strftime('%Y%m%d_%H%M%S_')
        if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            print(f'** Downloading images : message: {message.id}')
            dut.get_message_text(message)
            await dut.download_image(attachment.url, f'{file_prefix}{attachment.filename}')

    if msg_content == 'quit':
        quit()  

    elif msg_content == 'gd':
        mj.go_describe_mac('/tmp/demo.jpg')

    elif msg_content == 'gi':
        mj.go_imagine('a yellow rubber duck wearing red a silly hat')

    if msg_content.startswith("gg:"):
        msg_id = int(message.content.split(":")[1])
        print(f'** Attempt to get : message: {msg_id}')
        channel = message.channel
        msg = await channel.fetch_message(msg_id)
        dut.get_message_text(msg)

client.run(discord_config.discord_token)