from PIL import Image, ImageDraw, ImageFont
import textwrap
import time
import re
import bot_settings as bset

# img_target='test_images/merged_image.jpg'
# caption = 'an orange and black pair of scissors on a desk, in the style of webcam photography, sparse and simple, matte photo, sharp satire, applecore, english major, hard-edged compositions --ar 4:3)'
final_dir = './final'



def caption_wrap(caption):
    wrapper = textwrap.TextWrapper(width=50) 
    word_list = wrapper.wrap(text=caption) 
    return_text = ''
    print(type(word_list))
    word_list = word_list[0:2]
    for ii in word_list[:-1]:
        return_text = return_text + ii + '\n'
    return_text += word_list[-1]
    return return_text


def create_img_new(img_1, img_2, caption):
    print(f'Caption is {caption}')

    # caption =  re.sub('[ - @].*$', '', caption)
    caption =  re.sub(' \- @(.*$)', '', caption)

    caption = caption_wrap(caption)
    #Read the two images
    image1 = Image.open(img_1)
    image2 = Image.open(img_2)
    image1 = image1.resize((320, 240))
    image2 = image2.resize((320, 240))
    image1_size = image1.size
    image2_size = image2.size
    new_image = Image.new('RGB', ((2*image1_size[0])+30, 360), (250,250,250))
    new_image.paste(image1, (10,10))
    new_image.paste(image2, (image1_size[0]+20,10))

    # Front Image
    frontImage = Image.open(get_background(caption))
    frontImage = frontImage.resize((830, 240))
    frontImage = frontImage.convert("RGBA")
    new_image = new_image.convert('RGBA')

    # Calculate width to be at the center
    # width = (new_image.width - frontImage.width) // 2

    # Calculate height to be at the center
    # height = (new_image.height - frontImage.height) // 2

    # Paste the frontImage at (width, height)
    new_image.paste(frontImage, (-90, 180), frontImage)

    draw = ImageDraw.Draw(new_image)
    ifont = ImageFont.truetype(bset.get_font() , 26)
    draw.text((20,280), caption, font=ifont, fill=(0,0,0))

    file_prefix = time.strftime('%Y%m%d_%H%M%S')
    img_target = f'{final_dir}/{file_prefix}.png'
    new_image.save(img_target, 'png')
    new_image.show()

def do_create_img():
    print('Generating image')
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
    bset.set_caption('Pop art Caption a black cat laying on top of a yellow blanket, in the style of vivienne tam, graceful poses, smooth and shiny --ar 4:3 - ')
    bset.set_caption('futuristic  - ')
    bset.set_from_file('./test_images/01.JPG')
    bset.set_to_file('./test_images/02.JPG')
    do_create_img()
#     img_from = '/Users/saubury/git/saubury/midjourney-bot/test_images/02.JPG'
#     img_to = 'output/20230611_090933_Simon_Aubury_retro_pop_art-style_illustration_a_pokemon_mug_sit_818e9f5a-0a96-461e-8a63-e5dd37cc43ad_top_left.jpg'
#     img_caption = 'retro pop art-style illustration, a pokemon mug sits on an apple keyboard, in the style of captured spontaneity feeling, worthington whittredge, ue5, meticulous, sarah purser, emphasis on the process, yellow and silver --ar 4:3 - <@1003065257578741851>'

#     create_img_new(img_from, img_to, img_caption)
# create_img('test_images/before.jpg', 'test_images/after.jpg', caption_wrap(caption))