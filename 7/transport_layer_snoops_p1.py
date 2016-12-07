#!/usr/bin/env python3
import re


INPUT_FILE = 'input_p1.txt'


def main():
    # Read in IPs
    with open(INPUT_FILE, 'r') as f:
        ips = [l.rstrip() for l in f]


    # Regex for hypernet sequences
    hypernet_re = re.compile(r'\[(.+?)\]')

    tls_ips = list()
    for ip in ips:
        # Extract hypernet
        if any(abba_search(a) for a in hypernet_re.findall(ip)):
            continue

        # Extract non-hypernet
        if any(abba_search(s) for s in hypernet_re.sub(' ', ip).split()):
            tls_ips.append(ip)

    # Print number of tls ips
    print(len(tls_ips))


def abba_search(string):
    for i in range(len(string)-3):
        # Both characters can't be the same
        if string[i] == string[i+2]:
            continue

        # If we find any abba return True else at the end return False
        if string[i:i+2] == string[i+2:i+4][::-1]:
            return True
    return False



if __name__ == '__main__':
    main()
