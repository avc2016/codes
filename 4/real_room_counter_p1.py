#!/usr/bin/env python3
from collections import Counter
import re


INPUT_FILE = 'input_p1.txt'


class RoomCandidate():

    def __init__(self, room_data_string):
        self.room_data_string = room_data_string

        # Split tokens from data string into variables
        self.encrypted_name = str()
        self.sector_id = int()
        self.checksum = str()
        self.split_data_string()


    def split_data_string(self):
        # Get regex results
        data_re = re.compile(r'^(.+?)-([0-9]+)\[(.+?)\]$')
        re_result = data_re.match(self.room_data_string).groups()

        # Set instance variables
        self.encrypted_name = re_result[0].replace('-', '')
        self.sector_id = int(re_result[1])
        self.checksum = re_result[2]


    @property
    def is_room_real(self):
        '''Returns True if room is real'''
        return self.calculate_checksum() == self.checksum


    def calculate_checksum(self):
        # Get frequency of letters and sort them into hash of freq->letters
        freq_letters = dict()
        for k, v in Counter(self.encrypted_name).items():
            try:
                freq_letters[v].append(k)
            except KeyError:
                freq_letters[v] = [k]

        # Calculate checksum by gathering the five most common letters, ties
        # broken by alphabetisation
        checksum = list()
        # Iterate from the highest frequency to the lowest
        for freq in sorted(freq_letters, reverse=True):

            # Iterate all letters of this frequency in alphabetical order
            for letter in sorted(freq_letters[freq]):
                # Add to checksum if we have room, else return
                if len(checksum) < 5:
                    checksum.append(letter)
                else:
                    return ''.join(checksum)

        # In some cases we'll have exactly 5 letters to append, so the loop if
        # statement won't return. We return here instead
        return ''.join(checksum)


def main():
    # Read in and split room data
    with open(INPUT_FILE, 'r') as f:
        possible_rooms = [RoomCandidate(data_string.rstrip()) for data_string in f]

    # Find real rooms and calculate sector_id sum
    sector_id_sum = 0
    for possible_room in possible_rooms:
        if possible_room.is_room_real:
            sector_id_sum += possible_room.sector_id

    # Print sector_id_sum for final answer
    print(sector_id_sum)


if __name__ == '__main__':
    main()
