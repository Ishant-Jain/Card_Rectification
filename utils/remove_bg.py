import os
import cv2
import numpy as np
from rembg import remove

def remove_bg(input_file_path, filename, save=False):
    input_path = os.path.join(input_file_path, filename)
    input_image = cv2.imread(input_path)
    input_image_rgb = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

    # Removes background
    output_image = remove(input_image_rgb)
    output_image_np = np.array(output_image)
    image_with_transparent_bg = cv2.cvtColor(output_image_np, cv2.COLOR_RGBA2BGRA)

    # Save the image with transparency (use imwrite with PNG)
    if save:
        output_path = os.path.join(input_file_path, "without_bg")
        os.makedirs(output_path, exist_ok=True)
        output_file_path = os.path.join(output_path, filename.split(".")[0]+".png")
        cv2.imwrite(output_file_path, image_with_transparent_bg)

    return image_with_transparent_bg