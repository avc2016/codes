#!/usr/bin/env python3


INPUT_FILE = 'input_p2.txt'


def main():
    # Read in list of possible triangles
    with open(INPUT_FILE, 'r') as f:
        # Triangle sides are column major and are contiguous groups
        col_gen = (l.rstrip().split() for l in f)
        sides = [[int(s) for s in cols] for cols in col_gen]

        # Zip each row to get columns of triangles
        sides = zip(*sides)

        # Combine combine all lists into single list
        sides = [s for col in sides for s in col]

        # Gather sides into individual triangles
        possible_triangles = [sides[i:i+3] for i in range(0, len(sides), 3)]

    # Process triangles
    triangles = list()
    for possible_triangle in possible_triangles:
        # Test if is a triangle, add to running list if it is
        if is_triangle(possible_triangle):
            triangles.append(possible_triangle)

    # Print total number of triangles
    print(len(triangles))


def side_combinations_iter(sides):
    '''Returns combinations of sides plus the remaining side'''
    for i in range(len(sides)):
        for j in range(i+1, len(sides)):
            # Get the remaining side and return; surely there is a better way...
            k = [n for n in range(3) if n != i and n != j][0]
            yield sides[i], sides[j], sides[k]


def is_triangle(possible_triangle):
    for side_a, side_b, side_c in side_combinations_iter(possible_triangle):
        # Where side_a and side_b are tested to be greater than side_c
        if side_a + side_b <= side_c:
            return False

    # If all sides passed, return True
    return True


if __name__ == '__main__':
    main()
