import memegen
import sys
import random
import traceback

def run(argv):
    if len(argv) < 3:
        raise Exception("Not enough arguments!")
    fsrc, fdest = argv[1:3]
    resources_path = argv[3]
    strings = argv[4:]
    # 1/50th chance to ruin everything
    if random.random() < 0.02:
        terrible_strings = [random.choice(["yes", "wow", "very"]) for _ in range(20)]
        memegen.gen_meme(fsrc, fdest, resources_path, terrible_strings)
    else:
        memegen.gen_meme(fsrc, fdest, resources_path, strings)

if __name__ == "__main__":
    try:
        run(sys.argv)
        print "Done successfully"
        sys.exit(0)
    except Exception:
        # Print traceback
        traceback.print_exc(file=sys.stdout)
        print "Not done successfully"
        sys.exit(1)
