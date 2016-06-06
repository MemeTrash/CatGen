from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def gen_meme(file_src, file_dir, strings):
    """
    Generate a meme from an image and some text.
    """
    image = Image.open(file_src)
    drawer = ImageDraw.Draw(image)
    width, height = image.size()
    font_size = width // 30
    font = ImageFont.truetype("comic_sans_font.ttf", font_size)
    for string in strings:
        max_x = width - (len(string)*font_size)
        x, y = random.randint(0, width), random.randint(0, height)
        draw.text((x, y), string, (255, 255, 255), font=font)
    image.save(file_dir, "JPEG")

