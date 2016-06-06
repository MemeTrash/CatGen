from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random

def gen_meme(file_src, file_dir, strings):
    """
    Generate a meme from an image and some text.
    """
    image = Image.open(file_src)
    for string in strings:
        image = draw_text_on(image, string)
    image.save(file_dir, "JPEG")

def draw_text_on(image, text):
    """
    Args:
        image (Image): Image to draw on.
        text (str): String to draw.

    Returns:
        Image: Image with string drawn at a random location and rotation.
    """
    width, height = image.size
    font_size = width // 15
    font = ImageFont.truetype("resources/comic_sans_font.ttf", font_size)
    text_base = Image.new('RGBA', image.size, (255, 255, 255, 0))   # Base transparent image to write text on
    drawer = ImageDraw.Draw(text_base)
    max_x = width - (len(text)*font_size)
    max_y = height - font_size
    x, y = random.randint(0, max_x), random.randint(0, max_y)
    angle = random.uniform(-10, 10)
    drawer.text((x, y), text, (255, 255, 255), font=font)
    rotated_text = text_base.rotate(angle)
    result = Image.alpha_composite(image.convert('RGBA'), rotated_text)
    return result

