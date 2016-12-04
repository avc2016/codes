#!/usr/bin/env python3
from collections import Counter
import re


INPUT_FILE = 'input_p2.txt'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


class Room():

    def __init__(self, room_data_string):
        self.room_data_string = room_data_string

        # Split tokens from data string into variables
        self.encrypted_name = str()
        self.sector_id = int()
        self.checksum = str()
        self.split_data_string()

        # Other variable defined later
        self.descrypted_name = str()


    def split_data_string(self):
        # Get regex results
        data_re = re.compile(r'^(.+?)-([0-9]+)\[(.+?)\]$')
        re_result = data_re.match(self.room_data_string).groups()

        # Set instance variables
        self.encrypted_name = re_result[0]
        self.sector_id = int(re_result[1])
        self.checksum = re_result[2]


    def reverse_cipher(self):
        distance = self.sector_id % len(ALPHABET)

        decrypted_name_list = list()
        for letter in self.encrypted_name:
            if letter == '-':
                # Hypens are to be set to spaces
                decrypted_name_list.append(' ')
            else:
                # Get letter's current position and position after shift
                current_position = ALPHABET.find(letter)
                new_position = (current_position  + distance) % len(ALPHABET)

                # Add new letter to decrypted_name_list
                decrypted_name_list.append(ALPHABET[new_position])

        # Convert list to string and set instance variable
        self.decrypted_name = ''.join(decrypted_name_list)


    @property
    def has_northpole_objects(self):
        return 'northpole object storage' in self.decrypted_name


def main():
    # Read in and split room data
    with open(INPUT_FILE, 'r') as f:
        rooms = [Room(data_string.rstrip()) for data_string in f]

    # Reverse shift cipher and look for the string 'North Pole', break when found
    for room in rooms:
        room.reverse_cipher()
        if room.has_northpole_objects:
            print(room.sector_id)


if __name__ == '__main__':
    main()
