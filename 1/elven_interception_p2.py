#!/usr/bin/env python3
import argparse
import sys


INPUT_FILE = 'input_p2.txt'


class Position():

    def __init__(self, x, y, instructions):
        self.x = x
        self.y = y
        self.instructions = instructions

        # Direction is always initialised as 0
        self.direction = 0
        self.visited = set()
        self.visited.add((self.x, self.y))


    def follow_instructions(self):
        for rotation, distance in self.instructions:
            # First we must rotate before moving
            self.rotate_direction(rotation)

            # Move specific distance
            while distance:
                # Move along
                self.take_step()

                # Check if we've visited this position
                if (self.x, self.y) in self.visited:
                    print(abs(self.x) + abs(self.y))
                    sys.exit(0)
                else:
                    self.visited.add((self.x, self.y))

                # Decreament distance to go
                distance -= 1


    def rotate_direction(self, rotation):
        if rotation == 'R':
            self.direction = (self.direction + 90) % 360
        elif rotation == 'L':
            self.direction = (self.direction - 90) % 360
        else:
            raise TypeError


    def take_step(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 90:
            self.x += 1
        elif self.direction == 180:
            self.y -= 1
        elif self.direction == 270:
            self.x -= 1





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


if __name__ == '__main__':
    main()
