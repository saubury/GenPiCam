import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
import pyautogui as pg
import discord_config



load_dotenv()
client = commands.Bot(command_prefix="*", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Bot connected")

@client.event
async def on_message(message):

    msg = message.content
    print(message)

    # while prompt_counter < len(prompts):
    #     # Start Automation by typing "automation" in the discord channel
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
            # prompt_counter += 1

        # # continue Automation as soon Midjourney bot sends a message with attachment.
        # for attachment in message.attachments:
        #     time.sleep(3)
        #     pg.write('/imagine')
        #     time.sleep(5)
        #     pg.press('tab')
        #     pg.write(prompts[prompt_counter])
        #     time.sleep(3)
        #     pg.press('enter')
        #     time.sleep(5)
        #     prompt_counter += 1

    # # Stop Automation once all prompts are completed
    # quit()

client.run(discord_config.discord_token)