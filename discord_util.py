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
        return_text = embed.description

    # If still nothing try content
    if not return_text:
        return_text = msg.content

    return md_to_text(return_text)

        
def split_top_left_image(image_file):
    with Image.open(image_file) as im:
        # Get the width and height of the original image; calculate the middle points
        width, height = im.size
        mid_x = width // 2
        mid_y = height // 2
        top_left = im.crop((0, 0, mid_x, mid_y))
        return top_left

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
        f_response_img = f'{directory}/{input_folder}/{filename}'
        with open(f_response_img, 'wb') as f:
            f.write(response.content)
        print(f'Image downloaded: {filename}')
        input_file = os.path.join(input_folder, filename)

        file_prefix = os.path.splitext(filename)[0]
        # Split the image and save the output images with dynamic names in the output folder
        top_left = split_top_left_image(input_file)
        ret_path = os.path.join(output_folder, file_prefix + '_top_left.jpg')
        top_left.save(ret_path)
        os.remove(f_response_img)
        return ret_path
