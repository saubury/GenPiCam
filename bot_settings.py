

loc_test_images_dir = '/Users/saubury/git/saubury/midjourney-bot/test_images'
loc_is_pi = False

def print_settings():
    print(f'test_images_dir:{loc_test_images_dir}')
    print(f'is_pi:{loc_is_pi}')

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
        set_test_images_dir('/tmp')