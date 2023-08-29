import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from PIL import Image,ImageDraw
import numpy as np
import os

class Circle:
    def __init__(self):
        pass

    def load_img(self, filename: str):
        image = Image.open(filename).convert('L')
        image_width, image_height = image.size
        
        # Calculate the center coordinates
        center_x = image_width // 2
        center_y = image_height // 2

        # Define the radius of the circle
        circle_radius = min(center_x, center_y) // 1
        
        # Circular background.
        circle_mask = Image.new('L', (image_width, image_height), color=0)
        draw = ImageDraw.Draw(circle_mask)
        draw.ellipse((center_x - circle_radius, center_y - circle_radius, center_x + circle_radius, center_y + circle_radius), fill=255)
        outside_circle_image = Image.new('L', (image_width, image_height), color=0)
        outside_circle_image.paste(image, circle_mask)
        
        return outside_circle_image
    
    # Save the image in there respective folders.
    def save(self, image, filename):
        data_folder = os.path.join(os.getcwd(), 'Data')
        training_data_folder = os.path.join(data_folder, 'training_data')
        testing_data_folder = os.path.join(data_folder, 'testing_data')
        
        image_filename = os.path.basename(filename)
        
        if 'trainImgs' in filename:
            save_folder = training_data_folder
        elif 'testImgs' in filename:
            save_folder = testing_data_folder
        else:
            print(filename)
            raise ValueError("Unrecognized filename format")
        
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
            print(f'Folder created: {os.path.basename(save_folder)}')
        
        processed_image_path = os.path.join(save_folder, image_filename)
        image.save(processed_image_path)
        
        return f"Processed image saved at: {processed_image_path}"

if __name__ == '__main__':
    c = Circle()

    folders = [
        ('archive/trainImgs/trainImgs', 'trainingImgs'),
        ('archive/testImgs/testImgs', 'testImgs')
    ]
    
    for folder_path, keyword in folders:
        file_names = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
        for file_name in file_names:
            img_path = os.path.join(folder_path, file_name)
            loaded_image = c.load_img(img_path)
            img_save = c.save(loaded_image, img_path)
        
    print("processing Completed.")