from PIL import Image, ImageDraw, ImageFont
import textwrap
import time
import re
import bot_settings as bset

final_dir = './final'

def caption_wrap(caption):
    wrapper = textwrap.TextWrapper(width=50) 
    word_list = wrapper.wrap(text=caption) 
    return_text = ''
    for ii in word_list[:-1]:
        return_text = return_text + ii + '\n'
    return_text += word_list[-1]
    return return_text

def create_img_new(img_1, img_2, caption):
    # Removing trailing text
    caption =  re.sub(' \- [<]@(.*$)', '', caption)

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
    frontImage = Image.open(get_background(caption))
    frontImage = frontImage.resize((810, 560))
    frontImage = frontImage.convert("RGBA")
    new_image = new_image.convert('RGBA')

    # Paste the frontImage at (width, height)
    new_image.paste(frontImage, (-90, 60), frontImage)

    draw = ImageDraw.Draw(new_image)
    ifont = ImageFont.truetype(bset.get_font() , 26)
    draw.text((20,260), caption, font=ifont, fill=(0,0,0))

    file_prefix = time.strftime('%Y%m%d_%H%M%S')
    img_target = f'{final_dir}/{file_prefix}.png'
    new_image.save(img_target, 'png')
    new_image.show()

def do_create_img():
    create_img_new(bset.get_from_file(), bset.get_to_file(), bset.get_caption())

def get_background(caption):
    background_path = './input'

    if re.search('anime', caption, re.IGNORECASE):
        return f'{background_path}/box_brown.png'
    elif re.search('pop art', caption, re.IGNORECASE):
        return f'{background_path}/box_cyan.png'
    elif re.search('balloon', caption, re.IGNORECASE):
        return f'{background_path}/box_green.png'
    elif re.search('brush', caption, re.IGNORECASE):
        return f'{background_path}/box_grey.png'
    elif re.search('futuristic', caption, re.IGNORECASE):
        return f'{background_path}/box_orange.png'
    else:
        return f'{background_path}/box_yellow.png'

if __name__ == '__main__':
    img_from = './test_images/01.JPG'
    img_to = './test_images/02.JPG'
    img_caption = 'retro pop art-style illustration, a pokemon mug sits on an apple keyboard, in the style of captured spontaneity feeling, worthington whittredge, ue5, meticulous, sarah purser, emphasis on the process, yellow and silver --ar 4:3 - <@10030652575123123>'

    create_img_new(img_from, img_to, img_caption)
