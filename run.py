import pillow
import memegen
import sys

def run(argv):
    if len(argv) < 3:
        raise Exception("Not enough arguments!")
    fsrc, fdest = argv[0:2]
    strings = argv[2:]
    memegen.gen_image(fsrc, fdest, strings)

if __name__ == "__main__":
    run(sys.argv)

