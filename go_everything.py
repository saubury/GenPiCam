import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
import pyautogui as pg
import requests
from PIL import Image
import os
import discord_config

load_dotenv()
client = commands.Bot(command_prefix="*", intents=discord.Intents.all())
directory = os.getcwd()
print(directory)

def split_image(image_file):
    with Image.open(image_file) as im:
        # Get the width and height of the original image
        width, height = im.size
        # Calculate the middle points along the horizontal and vertical axes
        mid_x = width // 2
        mid_y = height // 2
        # Split the image into four equal parts
        top_left = im.crop((0, 0, mid_x, mid_y))
        top_right = im.crop((mid_x, 0, width, mid_y))
        bottom_left = im.crop((0, mid_y, mid_x, height))
        bottom_right = im.crop((mid_x, mid_y, width, height))
        return top_left, top_right, bottom_left, bottom_right

async def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:

        # Define the input and output folder paths
        input_folder = "input"
        output_folder = "output"

        # Check if the output folder exists, and create it if necessary
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Check if the input folder exists, and create it if necessary
        if not os.path.exists(input_folder):
            os.makedirs(input_folder)
        with open(f"{directory}/{input_folder}/{filename}", "wb") as f:
            f.write(response.content)
        print(f"Image downloaded: {filename}")
        input_file = os.path.join(input_folder, filename)

        if "UPSCALED_" not in filename:
            file_prefix = os.path.splitext(filename)[0]
            # Split the image
            top_left, top_right, bottom_left, bottom_right = split_image(input_file)
            # Save the output images with dynamic names in the output folder
            top_left.save(os.path.join(output_folder, file_prefix + "_top_left.jpg"))
            top_right.save(os.path.join(output_folder, file_prefix + "_top_right.jpg"))
            bottom_left.save(os.path.join(output_folder, file_prefix + "_bottom_left.jpg"))
            bottom_right.save(os.path.join(output_folder, file_prefix + "_bottom_right.jpg"))
        else:
            os.rename(f"{directory}/{input_folder}/{filename}", f"{directory}/{output_folder}/{filename}")
        # Delete the input file
        os.remove(f"{directory}/{input_folder}/{filename}")

@client.event
async def on_ready():
    print("Bot connected")

@client.event
async def on_message(message):
    msg = message.content
    print(message)

    for attachment in message.attachments:
        if "Upscaled by" in message.content:
            file_prefix = 'UPSCALED_'
        else:
            file_prefix = ''
        if attachment.filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            await download_image(attachment.url, f"{file_prefix}{attachment.filename}")

    if msg == 'quit':
        quit()  

    elif msg == 'describe':
        time.sleep(3)
        pg.press('tab')
        for i in range(1):
            time.sleep(3)
            pg.write('/describe')
            time.sleep(3)
            pg.press('tab')
            time.sleep(3)
            print(pg.position())
            pg.moveTo(x=461, y=1176, duration=1)
            time.sleep(1)
            pg.click()
            time.sleep(1)
            pg.hotkey('command','G', interval=0.1)
            pg.write('/tmp/demo.jpg')
            time.sleep(1)
            # close the file path
            pg.press('enter')    
            time.sleep(1)
            # close the browse window
            pg.press('enter')
            # complete the describe command
            time.sleep(2)
            pg.press('enter')        
            # final one
            time.sleep(2)
            pg.press('enter')
     

    elif msg == 'automation':
        time.sleep(3)
        pg.press('tab')
        for i in range(1):
            time.sleep(3)
            pg.write('/imagine')
            time.sleep(5)
            pg.press('tab')
            pg.write('a duck wearing a silly hat')
            time.sleep(3)
            pg.press('enter')
            time.sleep(5)


client.run(discord_config.discord_token)