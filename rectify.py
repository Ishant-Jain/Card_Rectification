import os
import cv2
import sys
import traceback
from utils.crop_image import crop_image
from utils.remove_bg import remove_bg

debug = True

def rectify_image(input_file_path, filename):
    try:
        bg_removed_image = remove_bg(input_file_path, filename, True)
        cropped_image = crop_image(bg_removed_image)
        cropped_path = os.path.join(input_file_path, "cropped")
        os.makedirs(cropped_path, exist_ok=True)
        cropped_file_path = os.path.join(cropped_path, filename.split(".")[0]+".png")
        cv2.imwrite(cropped_file_path, cropped_image)
        print("Task Completed Succesfully !!")
    except Exception as e:
        print("Ooops Some Exception Occured !!")
        if debug:
            print("Error Message:", str(e))
            print("Full Traceback:")
            traceback.print_exc()

if __name__ == "__main__":
    _, input_file_path, filename = sys.argv
    rectify_image(input_file_path, filename)
