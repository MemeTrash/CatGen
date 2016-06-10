# MemeGeneratorWow

This is the Python app that takes an image directory and text to generate a meme.

## Requirements

This uses Pillow, I guess :p (install with pip). Ubuntu 16.04 users with Python 2.7 can also install:
```
libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
```

## Usage

Simply by command line, do:

```
python run.py "image/src" "image/dest_file" "text1" "text2" ...
```

eg.

```
python run.py "images/doge_template.png" "images/meme.jpeg" "very doge" "wow"
```

## License

This uses the [MIT License](LICENSE).
