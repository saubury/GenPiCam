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

def do_create_img():
    print('Generating image')
    print_settings()
    create_img(loc_from_file, loc_to_file, caption_wrap(loc_caption))

# create_img('test_images/before.jpg', 'test_images/after.jpg', caption_wrap(caption))