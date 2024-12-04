import sys
from math import ceil
from math import log2
from flipflop import *
from helper import *
'''
    Code for generating the equations for an up-down counter that uses JK flip-flops.
    Counts down when x is 0
    "Don't cares" are encoded as -1
'''

base = int(input("Enter the base of the counter."))
state_count = ceil(log2(base))

homogenous = input("Would you like to use only one type of flip flop? (y/n)").lower()
if homogenous == 'y':
    flipper = input("Which type of flip flop would you like to use? (D, T, JK, SR)").lower()
    match flipper:
        case 'd':
            my_flip_flops = [D() for _ in range(state_count)]
        case 't':
            my_flip_flops = [T() for _ in range(state_count)]
        case 'jk':
            my_flip_flops = [JK() for _ in range(state_count)]
        case 'sr':
            my_flip_flops = [SR() for _ in range(state_count)]
        case _:
            sys.exit(1)
else:
    my_flip_flops = []
    for i in range(state_count):
        flipper = input(f"Which type of flip flop would you like to use for q{i}? (D, T, JK, SR)").lower()
        match flipper:
            case 'd':
                my_flip_flops.append(D())
            case 't':
                my_flip_flops.append(T())
            case 'jk':
                my_flip_flops.append(JK())
            case 'sr':
                my_flip_flops.append(SR())
            case _:
                sys.exit(1)

truth_table = build_truth_table(base, my_flip_flops)
counter_input = get_counter_input(base)
equation_data = build_equation_data(base, my_flip_flops, truth_table)

print()
display_eq_data(equation_data, counter_input)