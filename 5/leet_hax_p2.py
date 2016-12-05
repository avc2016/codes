#!/usr/bin/env python3
import hashlib


INPUT_FILE = 'input_p2.txt'


def main():
    # Read in door id
    with open(INPUT_FILE, 'r') as f:
        door_id = f.readline().rstrip()

    # Loop variables
    password = [None] * 8
    i = 0

    # Loop
    while any(p is None for p in password) and i < 10**7:
        # Increament counter
        i += 1

        # Get next hash string as bytes
        hash_string = '%s%s' % (door_id, i)
        hash_string_bytes = hash_string.encode()

        # Get MD5 hash and see if it starts with five zeros
        h = hashlib.md5(hash_string_bytes).hexdigest()
        if h.startswith('00000'):
            # Check if position will be a valid index, bounds not checked
            try:
                position = int(h[5])
            except ValueError:
                continue

            # Check if it's within bounds
            if position > 7:
                continue

            # Make sure we don't already have this position
            if password[position]:
                continue

            # Add to password if all conditions meet
            password[position] = h[6]

    # Print password
    print(*password, sep='')


if __name__ == '__main__':
    main()
