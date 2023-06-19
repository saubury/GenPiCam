import time

# State handler for async messaging with Discord

loc_test_images_dir = '/Users/saubury/git/saubury/midjourney-bot/test_images'
loc_is_pi = False
loc_automode = False
loc_ignorebutton = False
loc_caption = ''
loc_from_file = ''
loc_to_file = ''
loc_font = 'Arial.ttf'
loc_promptprefix = ''

def print_settings():
    print(f'caption:{loc_caption}')
    print(f'from_file:{loc_from_file}')
    print(f'to_file:{loc_to_file}')
    print(f'test_images_dir:{loc_test_images_dir}')
    print(f'is_pi:{loc_is_pi}')
    print(f'is_automode:{loc_automode}')
    print(f'is_ignorebutton:{loc_ignorebutton}')
    print(f'font:{loc_font}')
    print(f'promptprefix:{loc_promptprefix}')

def get_promptprefix():
    return loc_promptprefix

def set_promptprefix(promptprefix):
    global loc_promptprefix
    loc_promptprefix = promptprefix   

def get_font():
    return loc_font

def set_font(font):
    global loc_font
    loc_font = font        


def get_caption():
    return loc_caption

def set_caption(caption):
    global loc_caption
    loc_caption = caption

def get_from_file():
    return loc_from_file

def set_from_file(from_file):
    global loc_from_file
    loc_from_file = from_file

def get_to_file():
    return loc_to_file

def set_to_file(to_file):
    global loc_to_file
    loc_to_file = to_file

def get_test_images_dir():
    return loc_test_images_dir

def set_test_images_dir(test_images_dir):
    global loc_test_images_dir
    loc_test_images_dir = test_images_dir

def get_is_pi():
    return loc_is_pi

def get_automode():
    return loc_automode

def set_automode(automode):
    global loc_automode
    loc_automode = automode        


def get_ignorebutton():
    return loc_ignorebutton

def set_ignorebutton(ignorebutton):
    global loc_ignorebutton
    loc_ignorebutton = ignorebutton            


def set_is_pi(is_pi):
    global loc_is_pi
    loc_is_pi = is_pi

    if (is_pi):
        # over rides for Raspberry Pi
        set_test_images_dir('/home/simon/git/midjourney-bot/test_images')    
        set_font('LiberationSans-Regular.ttf')