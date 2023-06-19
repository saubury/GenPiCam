import pyautogui as pg
import time
import bot_settings as bset
import discord_util as dut

# Low level mid-journey bot intteractions with PyAutoGUI to control the mouse and keyboard to automate interactions


def go_imagine(prompt):

    time.sleep(3)
    pg.press('tab')
    time.sleep(3)
    pg.write('/imagine')
    time.sleep(5)
    pg.press('tab')
    pg.write(prompt)
    time.sleep(3)
    pg.press('enter')
    time.sleep(5)

def go_describe(image_path):
    bset.set_from_file(image_path)
    if bset.get_is_pi():
        go_describe_rasppi(image_path)
    else:
        go_describe_mac(image_path)


def go_describe_mac(image_path):

    time.sleep(3)
    pg.press('tab')
    time.sleep(3)
    pg.write('/describe')
    time.sleep(3)
    pg.press('tab')
    time.sleep(3)
    print(pg.position())
    # pg.moveTo(x=461, y=1176, duration=1)
    # pg.moveTo(x=454, y=812, duration=1) # mac laptop mode
    pg.moveTo(x=449, y=1195, duration=1) # mac main monitor
    time.sleep(1)
    pg.click()
    time.sleep(1)
    pg.hotkey('command','G', interval=0.1)
    pg.write(image_path)
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

def go_describe_rasppi(image_path):
    time.sleep(3)
    pg.write('/describe')
    time.sleep(3)
    pg.press('tab')
    time.sleep(3)
    print(pg.position())
    # (x=294, y=341)
    pg.moveTo(x=294, y=341, duration=1)
    time.sleep(1)
    pg.click()
    time.sleep(1)
    pg.write(image_path)
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
