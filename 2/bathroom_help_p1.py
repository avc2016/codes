#!/usr/bin/env python3


INPUT_FILE = 'input_p1.txt'
# Construct keypad matrix
M = 3
N = 3
BUTTONS = list(range(1,N*M+1))


class KeyPad():

    x_max = y_max = 3


    def __init__(self, instructions):
        self.x = 2
        self.y = 2
        self.instructions = instructions
        self.code = list()


    def follow_instructions(self):
        # For each line, follow the button sequence
        for sequence in self.instructions:
            self.follow_steps(sequence)

            # Get linear index and current button
            linear_index = self.subscript_to_linear(self.x, self.y, M)
            self.code.append(BUTTONS[linear_index])


    def follow_steps(self, sequence):
        for step in sequence:
            # Determine the position if we moved
            if step == 'U':
                if self.y - 1 > 0:
                    self.y -= 1
            elif step == 'D':
                if self.y + 1 <= self.y_max:
                    self.y += 1
            elif step == 'L':
                if self.x - 1 > 0:
                    self.x -= 1
            elif step == 'R':
                if self.x + 1 <= self.x_max:
                    self.x += 1


    @staticmethod
    def subscript_to_linear(x, y, size):
        return (y - 1) * size + x - 1


def main():
    # Read in instructions
    with open(INPUT_FILE, 'r') as f:
        instructions = tuple(l.rstrip() for l in f)

    # Initialise
    keypad = KeyPad(instructions)

    # Follow instructions
    keypad.follow_instructions()

    # Get code
    print(*keypad.code, sep='')


if __name__ == '__main__':
    main()
