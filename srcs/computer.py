import sys
import re

def solver(input):
    input = input.replace(' ', '')
    left, right = input.split('=') 
    leftdata = re.findall(r'([+-]?\d+(?:[.]\d*)?)[*]X\^(\d+)', left)
    rightdata = re.findall(r'([+-]?\d+(?:[.]\d*)?)[*]X\^(\d+)', right)
    left_dict = {int(exponent):float(coefficient) for (coefficient, exponent) in leftdata}
    right_dict = {int(exponent):float(coefficient) for (coefficient, exponent) in rightdata}
    print(left_dict)
    print(right_dict)
    
    for exponent, coefficient in right_dict.items():
        if exponent in left_dict:
            left_dict[exponent] -= coefficient

    print(left_dict)


def usage(program_name):
    use = f"""Usage: 
    python {program_name} \"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\""""
    print(use)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage(sys.argv[0])
        raise SystemExit("Program need ONE argument !")
    else:
        solver(sys.argv[1])
    
    
    