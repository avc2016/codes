#!/usr/bin/env python3
from collections import Counter


INPUT_FILE = 'input_p1.txt'


def main():
    # Read in transmissions
    with open(INPUT_FILE, 'r') as f:
        transmissions = [l.strip() for l in f]

    # Gather characters by their position within the transmissions
    transmission_positions = zip(*transmissions)

    # For each position, print the most common character; seems a little hacky
    # using operator[] twice
    message = [Counter(c).most_common(1)[0][0] for c in transmission_positions]
    print(*message, sep='')


if __name__ == '__main__':
    main()
