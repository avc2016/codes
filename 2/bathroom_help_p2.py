#!/usr/bin/env python3


INPUT_FILE = 'input_p2.txt'
# Construct keypad matrix
M = 5
N = 5
BUTTONS = (None,    None,   '1',   None,   None,
           None,    '2',    '3',    '4',    None,
           '5',     '6',    '7',    '8',   '9',
           None,    'A',    'B',    'C',    None,
           None,    None,   'D',    None,   None)


class KeyPad():

    x_max = y_max = M


    def __init__(self, instructions):
        self.x = 1
        self.y = 3
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
                if self.y - 1 > 0 and self.check_next_pos(self.x, self.y - 1):
                    self.y -= 1
            elif step == 'D':
                if self.y + 1 <= self.y_max and self.check_next_pos(self.x, self.y + 1):
                    self.y += 1
            elif step == 'L':
                if self.x - 1 > 0 and self.check_next_pos(self.x - 1, self.y):
                    self.x -= 1
            elif step == 'R':
                if self.x + 1 <= self.x_max and self.check_next_pos(self.x + 1, self.y):
                    self.x += 1


    def check_next_pos(self, x, y):
        # Get linear subscript
        linear_subscript = self.subscript_to_linear(x, y, M)
        return BUTTONS[linear_subscript] != None


    @staticmethod
    def subscript_to_linear(x, y, m):
        return (y - 1) * m + x - 1


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
