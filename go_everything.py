import discord
from discord.ext import commands
import discord_config
import midjourney as mj
import discord_util as dut
import mj_images as mji
import bot_settings as bset
import rasp_pi as rp
import time
import configparser
import argparse


client = commands.Bot(command_prefix='*', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot connected')

@client.event
async def on_message(message):
    msg_content = message.content
    mj.get_mj_message(message)

    for attachment in message.attachments:
        print(f'** Attachment found : message: {message.id}')
        file_prefix = time.strftime('%Y%m%d_%H%M%S_')
        if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
            print(f'** Downloading images : message: {message.id}')

            cap_msg = dut.get_message_text(message)
            print ('>>')
            print(cap_msg)
            bset.set_caption(cap_msg)
            print ('<<')

            ret_path = await dut.download_image(attachment.url, f'{file_prefix}{attachment.filename}')
            bset.set_to_file(ret_path)
            if (bset.get_automode()):
                mji.do_create_img()   
                bset.set_ignorebutton(False)             

    if msg_content == 'quit':
        quit()  

    elif msg_content == 'gi':
        mj.go_imagine('a yellow rubber duck wearing red a silly hat')

    elif msg_content == 'gp':
        bset.print_settings()

    elif msg_content == 'gtest':
        bset.set_caption('Caption a black cat laying on top of a yellow blanket, in the style of vivienne tam, graceful poses, smooth and shiny --ar 4:3 - ')
        bset.set_from_file('./test_images/01.JPG')
        bset.set_to_file('./test_images/02.JPG')
        mji.do_create_img()

    elif msg_content == 'gg':
        mji.do_create_img()

    elif msg_content.startswith('gd:'):
        msg_ref = message.content.split(":")[1]
        test_img_path = bset.get_test_images_dir()
        file_in = f'{test_img_path}/{msg_ref}.JPG'
        print(f'FILE IN: {file_in}')
        mj.go_describe(file_in)
        

    elif msg_content.startswith("ggm:"):
        msg_id = int(message.content.split(":")[1])
        print(f'** Attempt to get : message: {msg_id}')
        channel = message.channel
        msg = await channel.fetch_message(msg_id)
        cap_msg = dut.get_message_text(msg)
        print ('>>')
        print(cap_msg)
        print ('<<')

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument(
        '--enablePi',
        help='Whether to enable Raspberry Pi buttons',
        action='store_true',
        required=False,
        default=False)
    
    parser.add_argument(
        '--auto',
        help='Whether to automatically chain actions',
        action='store_true',
        required=False,
        default=False)
    
    args = parser.parse_args()

    bset.set_automode(args.auto)

    if (args.enablePi):
        bset.set_is_pi(True)
        rp.setup_gpio()

    client.run(discord_config.discord_token)

if __name__ == '__main__':
    main()
