from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random

def gen_meme(file_src, file_dir, strings):
    """
    Generate a meme from an image and some text.
    """
    image = Image.open(file_src)
    if file_src[:-4] == file_dir[:-4] == ".gif":
        image = animate_gif(image, file_dir, strings)
    for string in strings:
        image = draw_text_on(image, string)
    # 1/200 chance to add another meme ontop of original image
    if random.random() < 1:
        image = add_extra_meme(image)
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
    # 1/4 chance to print text in red instead of white
    if random.random() < 0.25:
        drawer.text((x, y), text, (255, 0, 0), font=font)
    else:
        drawer.text((x, y), text, (255, 255, 255), font=font)
    rotated_text = text_base.rotate(angle)
    result = Image.alpha_composite(image.convert('RGBA'), rotated_text)
    return result

def add_extra_meme(orig_img):
    """
    Add another meme ontop of picture. Low chance of happening.

    Args:
        orig_img (Image): Image to add meme onto.

    Returns:
        Image: Image with meme ontop in random location.

    """
    meme_images = ["feels_meme.png", "happy_meme.jpeg", "nyan_meme.jpeg"]
    extra_meme = Image.open("resources/more_memes/" + random.choice(meme_images)).convert('RGB')
    new_width = orig_img.size[1] // 8;
    new_height = orig_img.size[0] // 8;
    smaller_meme = extra_meme.resize((new_width, new_height), Image.ANTIALIAS)
    orig_img.paste(smaller_meme, (random.randint(0, orig_img.size[0]), random.randint(0, orig_img.size[1])))
    return orig_img

def animate_gif(image, dest_path, strings):
    """
    Takes an image and produces + saves an animated gif.
    Gif is just original image with texts each placed randomly around image at each frame.

    Args:
        image (Image): Image to convert to animated gif.
        dest_path (str): Destination file path.
        strings (list[str]): List of strings to display.
    """
    try:
        while True:
            image = draw_text_on(image)
            image.seek(image.tell()+1)
    except EOFError:
        image.save(dest_path, "GIF")

