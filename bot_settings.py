

loc_test_images_dir = '/Users/saubury/git/saubury/midjourney-bot/test_images'
loc_is_pi = False
loc_automode = False
loc_ignorebutton = False

def print_settings():
    print(f'test_images_dir:{loc_test_images_dir}')
    print(f'is_pi:{loc_is_pi}')
    print(f'is_automode:{loc_automode}')
    print(f'is_ignorebutton:{loc_ignorebutton}')

def get_test_images_dir():
    return loc_test_images_dir

def set_test_images_dir(test_images_dir):
    global loc_test_images_dir
    loc_test_images_dir = test_images_dir

def get_is_pi():
    return loc_is_pi

def set_is_pi(is_pi):
    global loc_is_pi
    loc_is_pi = is_pi

    if (is_pi):
        # over rides for Rasapberry Pi
        set_test_images_dir('/home/simon/git/midjourney-bot/test_images')

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