import argparse
import os
import cv2
from PIL import Image


def get_video_data(image_path):
    img = Image.open(image_path)
    width, height = img.size

    # RGB values for color
    img = img.convert("RGB")
    color_map = img.load()

    # return color_map, width, height

    # Turn data into plain lists
    rows = []
    for y in range(height):
        cols = []
        for x in range(width):
            color_val = list(color_map[x, y])
            cols.append(color_val)
        
        rows.append(cols)

    color = rows

    return color

def cprint(text, color, end="\n"):
    r, g, b = color
    print(f"\x1b[38;2;{r};{g};{b}m{text}\x1b[0m", end=end)

def cineshell(filepath):
    data = get_pixel_data(filepath)

    for row in data:
        for pixel in row:
            cprint("█", pixel, end="")
        print()

parser = argparse.ArgumentParser(description="Display an image in the terminal.")
parser.add_argument("-fp", "--filepath", type=str, help="Path to image file", required=True, dest="filepath")
filepath = parser.parse_args().filepath

cineshell(filepath)