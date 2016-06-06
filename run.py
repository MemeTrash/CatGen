import memegen
import sys
import random
import traceback

def run(argv):
    if len(argv) < 3:
        raise Exception("Not enough arguments!")
    fsrc, fdest = argv[1:3]
    strings = argv[3:]
    # 1/50th chance to ruin everything
    if random.random() < 0.02:
        terrible_strings = [random.choice(["yes", "wow", "very"]) for _ in range(20)]
        memegen.gen_meme(fsrc, fdest, terrible_strings)
    else:
        memegen.gen_meme(fsrc, fdest, strings)

if __name__ == "__main__":
    try:
        run(sys.argv)
        sys.exit(0)
    except Exception:
        # Print traceback
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)
