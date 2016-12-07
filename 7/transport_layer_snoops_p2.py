#!/usr/bin/env python3
import re


INPUT_FILE = 'input_p2.txt'


def main():
    # Read in IPs
    with open(INPUT_FILE, 'r') as f:
        ips = [l.rstrip() for l in f]


    # Regex for hypernet sequences
    hypernet_re = re.compile(r'\[(.+?)\]')

    ssl_ips = list()
    for ip in ips:
        # Extract hypernet and collect all babs
        babs = list()
        for hs in hypernet_re.findall(ip):
            babs.extend(bab_search(hs))

        # Convert to abas
        abas = [s[1] + s[0] + s[1] for s in babs]

        # Search stdnet for any abas
        if any(aba_search(s, abas) for s in hypernet_re.sub(' ', ip).split()):
            ssl_ips.append(ip)


    # Print number of tls ips
    print(len(ssl_ips))


def aba_search(string, abas):
    # Find any aba in the string
    for aba in abas:
        # Return True if found else return False later
        if aba in string:
            return True
    return False


def bab_search(string):
    babs = list()
    for i in range(len(string)-2):
        # First two characters can't be the same
        if string[i] == string[i+1]:
            continue

        # If we find any bab string add to running list
        if string[i] == string[i+2]:
            babs.append(string[i:i+3])

    return babs


if __name__ == '__main__':
    main()
