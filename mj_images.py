from PIL import Image, ImageDraw, ImageFont
import textwrap
import time

# img_target='test_images/merged_image.jpg'
# caption = 'an orange and black pair of scissors on a desk, in the style of webcam photography, sparse and simple, matte photo, sharp satire, applecore, english major, hard-edged compositions --ar 4:3)'
final_dir = './final'

loc_caption = ''
loc_from_file = ''
loc_to_file = ''

def print_settings():
    print(f'Caption {loc_caption}')
    print(f'From {loc_from_file}')
    print(f'To {loc_to_file}')

def set_caption(caption):
    global loc_caption
    loc_caption = caption

def set_from_file(from_file):
    global loc_from_file
    loc_from_file = from_file

def set_to_file(to_file):
    global loc_to_file
    loc_to_file = to_file

def caption_wrap(caption):
    wrapper = textwrap.TextWrapper(width=50) 
    word_list = wrapper.wrap(text=caption) 
    return_text = ''
    for ii in word_list[:-1]:
        return_text = return_text + ii + '\n'
    return_text += word_list[-1]
    return return_text

def create_img(img_1, img_2, caption):
    #Read the two images
    image1 = Image.open(img_1)
    image2 = Image.open(img_2)
    image1 = image1.resize((320, 240))
    image2 = image2.resize((320, 240))
    image1_size = image1.size
    image2_size = image2.size
    new_image = Image.new('RGB', (2*image1_size[0], image1_size[1]*2), (250,250,250))
    new_image.paste(image1, (0,0))
    new_image.paste(image2, (image1_size[0],0))

    draw = ImageDraw.Draw(new_image)
    ifont = ImageFont.truetype('Arial.ttf', 26)
    draw.text((20,280), caption, font=ifont, fill=(255,0,0))

    file_prefix = time.strftime('%Y%m%d_%H%M%S')
    img_target = f'{final_dir}/{file_prefix}.jpg'
    new_image.save(img_target, 'JPEG')
    new_image.show()

def create_img_new(img_1, img_2, caption):

    # initializing sub string
    sub_str = "<@1003065257578741851>"
    
    # slicing off after length computation
    caption = caption[:caption.index(sub_str) ]

    caption = caption_wrap(caption)
    #Read the two images
    image1 = Image.open(img_1)
    image2 = Image.open(img_2)
    image1 = image1.resize((320, 240))
    image2 = image2.resize((320, 240))
    image1_size = image1.size
    image2_size = image2.size
    new_image = Image.new('RGB', (2*image1_size[0], image1_size[1]*2), (250,250,250))
    new_image.paste(image1, (0,0))
    new_image.paste(image2, (image1_size[0],0))

    # Front Image
    frontImage = Image.open('input/box.png')
    frontImage = frontImage.resize((810, 560))
    frontImage = frontImage.convert("RGBA")
    new_image = new_image.convert('RGBA')

    # Calculate width to be at the center
    # width = (new_image.width - frontImage.width) // 2

    # Calculate height to be at the center
    # height = (new_image.height - frontImage.height) // 2

    # Paste the frontImage at (width, height)
    new_image.paste(frontImage, (-90, 60), frontImage)

    draw = ImageDraw.Draw(new_image)
    ifont = ImageFont.truetype('Arial.ttf', 26)
    draw.text((20,260), caption, font=ifont, fill=(0,0,0))

    file_prefix = time.strftime('%Y%m%d_%H%M%S')
    img_target = f'{final_dir}/{file_prefix}.png'
    new_image.save(img_target, 'png')
    new_image.show()

def do_create_img():
    print('Generating image')
    print_settings()
    # create_img(loc_from_file, loc_to_file, caption_wrap(loc_caption))
    create_img_new(loc_from_file, loc_to_file, loc_caption)

if __name__ == '__main__':
    img_from = '/Users/saubury/git/saubury/midjourney-bot/test_images/02.JPG'
    img_to = 'output/20230611_090933_Simon_Aubury_retro_pop_art-style_illustration_a_pokemon_mug_sit_818e9f5a-0a96-461e-8a63-e5dd37cc43ad_top_left.jpg'
    img_caption = 'retro pop art-style illustration, a pokemon mug sits on an apple keyboard, in the style of captured spontaneity feeling, worthington whittredge, ue5, meticulous, sarah purser, emphasis on the process, yellow and silver --ar 4:3 - <@1003065257578741851>'

    create_img_new(img_from, img_to, img_caption)
# create_img('test_images/before.jpg', 'test_images/after.jpg', caption_wrap(caption))