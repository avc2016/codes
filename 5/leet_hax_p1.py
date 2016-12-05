#!/usr/bin/env python3
import hashlib


INPUT_FILE = 'input_p1.txt'


def main():
    # Read in door id
    with open(INPUT_FILE, 'r') as f:
        door_id = f.readline().rstrip()

    # Loop variables
    password = list()
    i = 0

    # Loop
    while len(password) < 8 and i < 10**7:
        # Increament counter
        i += 1

        # Get next hash string as bytes
        hash_string = '%s%s' % (door_id, i)
        hash_string_bytes = hash_string.encode()

        # Get MD5 hash and see if it starts with five zeros
        h = hashlib.md5(hash_string_bytes).hexdigest()
        if h.startswith('00000'):
            password.append(h[5])

    # Print password
    print(*password, sep='')


if __name__ == '__main__':
    main()
