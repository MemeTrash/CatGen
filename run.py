import memegen
import sys

def run(argv):
    if len(argv) < 3:
        raise Exception("Not enough arguments!")
    fsrc, fdest = argv[1:3]
    strings = argv[3:]
    memegen.gen_meme(fsrc, fdest, strings)

if __name__ == "__main__":
    run(sys.argv)

