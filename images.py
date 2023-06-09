from PIL import Image, ImageDraw, ImageFont
import textwrap

img_target='test_images/merged_image.jpg'
caption = 'an orange and black pair of scissors on a desk, in the style of webcam photography, sparse and simple, matte photo, sharp satire, applecore, english major, hard-edged compositions --ar 4:3)'

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
    ifont = ImageFont.truetype('Arial.ttf', 22)
    draw.text((20,280), caption, font=ifont, fill=(255,0,0))

    new_image.save(img_target, 'JPEG')
    new_image.show()


create_img('test_images/before.jpg', 'test_images/after.jpg', caption_wrap(caption))