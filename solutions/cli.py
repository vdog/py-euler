import argparse
import sys
import importlib

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    args = parser.parse_args()
    print(args.integers)
    import_me = "solutions.century1.decade1.problem1"
    if args.integers[0] < 100:
        if args.integers[0] <= 10:
            import_me = "solutions.century1.decade1.problem{}".format(args.integers[0])
            print(import_me)
    mod = importlib.import_module(import_me)
    mod.run()


