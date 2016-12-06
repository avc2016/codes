#!/usr/bin/env python3
from collections import Counter


INPUT_FILE = 'input_p2.txt'


def main():
    # Read in transmissions
    with open(INPUT_FILE, 'r') as f:
        transmissions = [l.strip() for l in f]

    # Gather characters by their position within the transmissions
    transmission_positions = zip(*transmissions)

    # For each position, print the least common character
    for transmission_position in transmission_positions:
        counts = Counter(transmission_position)
        print(sorted(counts, key=lambda k: counts[k])[0], end='')

    # Print trailing new line
    print('\n', end='')


if __name__ == '__main__':
    main()
