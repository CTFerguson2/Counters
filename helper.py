from math import log2
from math import ceil
from sympy import symbols
from sympy.logic import SOPform
# from flipflop import *


def b_arr(number, width):
    return [int(digit) for digit in bin(number)[2:].zfill(width)]


def build_truth_table(base, my_flip_flops):
    state_count = ceil(log2(base))  # Number of states
    end = 2 ** (state_count + 1)  # The highest bin number representable with the number of states
    truth_table = []
    for num in range(0, end):  # Builds truth table
        b_num = b_arr(num, state_count + 1)

        state = num - (b_num[0] * (2 ** state_count))
        b_state = b_arr(state, state_count)

        if state >= base:
            b_nxt_state = [-1 for _ in range(0, state_count)]  # Don't care about state transitions for invalid states
        else:
            nxt_state = (state + (1 if b_num[0] else -1)) % base
            b_nxt_state = b_arr(nxt_state, state_count)

        row = {
            "x": b_num[0],  # Counting up or down?
            "state": b_state,  # [qn, ..., q0]
            "next_state": b_nxt_state,  # [qn*, ..., q0*]
        }

        for i in range(state_count):  # Do the row's flipflops
            flipflop = my_flip_flops[i]  # my_flip_flops[0] is for q(state_count - 1)
            true_index = (state_count - 1) - i
            row[f'{flipflop.style}{i}'] = flipflop.map(row['state'][true_index], row['next_state'][true_index])

        truth_table.append(row)
    return truth_table


def get_counter_input(base):
    state_count = ceil(log2(base))
    in_string = f"x {' '.join([f'q{state_count - (i + 1)}' for i in range(state_count)])}"  # qn, ..., q0
    return symbols(in_string)


def build_equation_data(base, my_flip_flops, truth_table):
    state_count = ceil(log2(base))
    equation_data = [  # Index tells you which flipflop it is
        {f"{item}": {"minterms": [], "dontcares": []} for item in my_flip_flops[i].style} for i in range(state_count)
    ]
    for row in truth_table:  # Populate equation data
        for col in range(len(my_flip_flops)):
            flipflop = my_flip_flops[col]
            # print(row)
            flipflop_values = row[f'{flipflop.style}{col}']
            for item in range(flipflop.indices):
                if flipflop_values[item] == 1:
                    equation_data[col][flipflop.style[item]]["minterms"].append([row['x']] + row["state"])
                elif flipflop_values[item] == -1:
                    equation_data[col][flipflop.style[item]]["dontcares"].append([row['x']] + row["state"])
    return equation_data


def display_eq_data(equation_data, counter_input):
    for flipflop in range(len(equation_data)):
        for item, data in equation_data[flipflop].items():
            print(f"{item}{flipflop}: {SOPform(counter_input, data['minterms'], data['dontcares'])}")
