#!/usr/bin/env python3
import argparse
import sys


INPUT_FILE = 'input.txt'


class Position():

    def __init__(self, x, y, instructions):
        self.x = x
        self.y = y
        self.instructions = instructions

        # Direction is always initialised as 0
        self.direction = 0


    def follow_instructions(self):
        for rotation, distance in self.instructions:
            # First we must rotate before moving
            self.rotate_direction(rotation)

            # Move specific distance
            self.move_distance(distance)


    def rotate_direction(self, rotation):
        if rotation == 'R':
            self.direction = (self.direction + 90) % 360
        elif rotation == 'L':
            self.direction = (self.direction - 90) % 360
        else:
            raise TypeError


    def move_distance(self, distance):
        if self.direction == 0:
            self.y += distance
        elif self.direction == 90:
            self.x += distance
        elif self.direction == 180:
            self.y -= distance
        elif self.direction == 270:
            self.x -= distance


def main():
    # Read in instructions
    with open(INPUT_FILE, 'r') as f:
        instructions = [(el[0], int(el[1:])) for el in f.readline().rstrip().split(', ')]

    # Initalise position and direction
    direction = 0
    position = Position(0, 0, instructions)

    # Follow instructions
    position.follow_instructions()

    # Print resulting position
    print(abs(position.x) + abs(position.y))


if __name__ == '__main__':
    main()
