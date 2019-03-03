import argparse
import pyperclip

from pyclip.counterstring import generate_counterstring


def check_length(length):
    try:
        length = int(length)
    except Exception:
        raise argparse.ArgumentTypeError('length must be an integer')
    if length < 1:
        raise argparse.ArgumentTypeError('length must be greater than 0')
    return length


def pyclip(desired_marker, desired_length):
    return generate_counterstring(desired_marker, desired_length)


def main():
    parser = argparse.ArgumentParser(description='A python counterstring generator')
    parser.add_argument(type=check_length, dest='length', default=1000, nargs='?')
    args = parser.parse_args()
    my_counterstring = pyclip('*', args.length)
    pyperclip.copy(my_counterstring)
    print('Counterstring copied to clipboard. Ready to paste!')


if __name__ == '__main__':
    main()
