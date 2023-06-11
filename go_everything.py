import discord
from discord.ext import commands
import discord_config
import midjourney as mj
import discord_util as dut
import mj_images as mji
import time




client = commands.Bot(command_prefix='*', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot connected')

@client.event
async def on_message(message):
    msg_content = message.content
    print(message)

    for attachment in message.attachments:
        print(f'** Attachment found : message: {message.id}')
        file_prefix = time.strftime('%Y%m%d_%H%M%S_')
        if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            print(f'** Downloading images : message: {message.id}')

            cap_msg = dut.get_message_text(message)
            print ('>>')
            print(cap_msg)
            mji.set_caption(cap_msg)
            print ('<<')

            ret_path = await dut.download_image(attachment.url, f'{file_prefix}{attachment.filename}')
            mji.set_to_file(ret_path)

    if msg_content == 'quit':
        quit()  

    elif msg_content == 'gi':
        mj.go_imagine('a yellow rubber duck wearing red a silly hat')

    elif msg_content == 'gp':
        mji.print_settings()

    elif msg_content == 'gg':
        # mji.set_caption('Caption a black cat laying on top of a yellow blanket, in the style of vivienne tam, graceful poses, smooth and shiny --ar 4:3 - ')
        # mji.set_from_file('/Users/saubury/git/saubury/midjourney-bot/test_images/01.JPG')
        # mji.set_to_file('output/20230610_223745_Simon_Aubury_a_black_cat_laying_on_top_of_a_yellow_blanket_in_t_6bbdf148-1a97-4548-8a1d-18d996c4a7fa_top_left.jpg')
        mji.do_create_img()

    elif msg_content.startswith('gd:'):
        msg_ref = message.content.split(":")[1]
        file_in = f'/Users/saubury/git/saubury/midjourney-bot/test_images/{msg_ref}.JPG'
        print(f'FILE IN: {file_in}')
        mj.go_describe_mac(file_in)
        mji.set_from_file(file_in)

    elif msg_content.startswith("ggm:"):
        msg_id = int(message.content.split(":")[1])
        print(f'** Attempt to get : message: {msg_id}')
        channel = message.channel
        msg = await channel.fetch_message(msg_id)
        cap_msg = dut.get_message_text(msg)
        print ('>>')
        print(cap_msg)
        print ('<<')

client.run(discord_config.discord_token)