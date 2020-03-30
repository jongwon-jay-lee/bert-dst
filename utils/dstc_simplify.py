import json
import re
import sys
import argparse


def simplify_dstc2(dialog_filename, new_dialog_filename):
    with open(dialog_filename) as f:
        print('Read: {}'.format(dialog_filename))
        dst_set = json.load(f)

    length = len(dst_set)
    for i, dial in enumerate(dst_set):
        for turn in dial['dialogue']:
            turn.pop('asr', None)
        if i % 1000 == 0:
            print("{} dialogs processed".format(i))
    print("{} dialogs Done".format(length))

    with open(new_dialog_filename, 'w') as new_f:
        print('Write on {}'.format(new_dialog_filename))
        json.dump(dst_set, new_f, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="dstc2 original file")
    parser.add_argument("--output", help="dstc2 simplified output file")
    args = parser.parse_args()

    simplify_dstc2(args.input, args.output)
