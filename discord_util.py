from PIL import Image
import os
import requests
import markdown 
from bs4 import BeautifulSoup 

directory = os.getcwd()

def md_to_text(md):
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features='html.parser')
    return soup.get_text()

def get_message_text(msg):
    return_text=''

    # Extract text is within an embed 
    embeds = msg.embeds # return list of embeds
    for embed in embeds:
        print('** Found embed')
        return_text = embed.description

    # If still nothing try content
    if not return_text:
        return_text = msg.content

    return md_to_text(return_text)

        
def split_image(image_file):
    with Image.open(image_file) as im:
        # Get the width and height of the original image
        width, height = im.size
        # Calculate the middle points along the horizontal and vertical axes
        mid_x = width // 2
        mid_y = height // 2
        # Split the image into four equal parts
        top_left = im.crop((0, 0, mid_x, mid_y))
        top_right = im.crop((mid_x, 0, width, mid_y))
        bottom_left = im.crop((0, mid_y, mid_x, height))
        bottom_right = im.crop((mid_x, mid_y, width, height))
        return top_left, top_right, bottom_left, bottom_right

async def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:

        # Define the input and output folder paths
        input_folder = 'input'
        output_folder = 'output'

        # Check if the output folder exists, and create it if necessary
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Check if the input folder exists, and create it if necessary
        if not os.path.exists(input_folder):
            os.makedirs(input_folder)
        with open(f'{directory}/{input_folder}/{filename}', 'wb') as f:
            f.write(response.content)
        print(f'Image downloaded: {filename}')
        input_file = os.path.join(input_folder, filename)

        if 'UPSCALED_' not in filename:
            file_prefix = os.path.splitext(filename)[0]
            # Split the image
            top_left, top_right, bottom_left, bottom_right = split_image(input_file)
            # Save the output images with dynamic names in the output folder
            top_left.save(os.path.join(output_folder, file_prefix + '_top_left.jpg'))
            top_right.save(os.path.join(output_folder, file_prefix + '_top_right.jpg'))
            bottom_left.save(os.path.join(output_folder, file_prefix + '_bottom_left.jpg'))
            bottom_right.save(os.path.join(output_folder, file_prefix + '_bottom_right.jpg'))
        else:
            os.rename(f'{directory}/{input_folder}/{filename}', f'{directory}/{output_folder}/{filename}')
        # Delete the input file
        os.remove(f'{directory}/{input_folder}/{filename}')

        ret_path = os.path.join(output_folder, file_prefix + '_top_left.jpg')
        return ret_path
