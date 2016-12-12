#!/usr/bin/env python3
import re


INPUT_FILE = 'input_p1.txt'


WIDTH = 50
HEIGHT = 6


class Screen():

    rectangle_ins_re = re.compile(r'^rect ([0-9]+)x([0-9]+)$')
    rotate_ins_re = re.compile(r'^rotate (.+?) (?:x|y)=([0-9]+) by ([0-9]+)$')


    def __init__(self, instructions):
        self.pixels = [[0] * HEIGHT for i in range(WIDTH)]
        self.instructions = instructions


    def execute_instructions(self):
        for instruction in self.instructions:
            if instruction.startswith('rect'):
                # Turn on a rectangle of pixels
                self.turn_on_rectangle(instruction)

            elif instruction.startswith('rotate'):
                # Move row or column of pixels
                self.move_pixels(instruction)
            else:
                # Should never reach this clause
                raise ValueError


    def turn_on_rectangle(self, instruction):
        # Get dimensions of rectangle to turn on
        width, height = self.rectangle_ins_re.match(instruction).groups()

        # Turn on required pixels, origin is always (0, 0)
        for i in range(int(width)):
            for j in range(int(height)):
                self.pixels[i][j] = 1


    def move_pixels(self, instruction):
        # Get info from instruction
        element, index, distance = self.rotate_ins_re.match(instruction).groups()
        index = int(index)
        distance = int(distance)


        if element == 'column':
            # Modulo of distance to determine new breakpoint in pixel vector
            mod_distance = distance % HEIGHT

            # The breakpoint will be calculated relative to the end of the vector
            break_index = -1 * mod_distance

            # Get current values of pixels and slice vector at new breakpoint
            values = self.pixels[index]
            rotated_values = values[break_index:] + values[:break_index]

            # Update the pixels on screen
            self.pixels[index] = rotated_values

        elif element == 'row':
            # Modulo of distance to determine new breakpoint in pixel vector
            mod_distance = distance % WIDTH

            # The breakpoint will be calculated relative to the end of the vector
            break_index = -1 * mod_distance

            # Get current values of pixels and slice vector at new breakpoint
            values = [self.pixels[i][index] for i in range(WIDTH)]
            rotated_values = values[break_index:] + values[:break_index]

            # Update the pixels on screen
            for i in range(WIDTH):
                self.pixels[i][index] = rotated_values[i]

        else:
            # We should be either row or column
            raise ValueError



    def __str__(self):
        row_strings = list()
        for row in zip(*self.pixels):
            rs = ' '.join([str(el) for el in row])
            rs = rs.replace('0', '.')
            rs = rs.replace('1', '#')
            row_strings.append(rs)
        return '\n'.join(row_strings)


def main():
    # Read instructions
    with open(INPUT_FILE, 'r') as f:
        instructions = [l.rstrip() for l in f]

    # Init screen and execute instructions
    screen = Screen(instructions)
    screen.execute_instructions()

    # Print out the current screen state and calculate number of on pixels
    print(screen)
    pixels_on = sum([p for col in screen.pixels for p in col])
    print(sum([el for col in screen.pixels for el in col]))


if __name__ == '__main__':
    main()
