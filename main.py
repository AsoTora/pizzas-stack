from errno import EIDRM
import sys
import ast


def equalStacks(h1: list, h2: list, h3: list):
    """
    Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. 
    This means you must remove zero or more cylinders from the top of zero or more of the three stacks until
    they are all the same height, then return the height.

    assume the input is always correct
    """
    if sum(h1) == sum(h2) == sum(h3):
        return sum(h1)

    sorted_stacks = sorted(list(locals().values()), key=sum, reverse=True)

    sorted_stacks[0].pop()
    hight = sum(sorted_stacks[0])

    while sum(sorted_stacks[1]) > hight:
        sorted_stacks[1].pop()

    while sum(sorted_stacks[2]) > hight:
        sorted_stacks[2].pop()

    return equalStacks(*sorted_stacks)


if __name__ == "__main__":

    try:
        params = []
        for arg in sys.argv[1:]:
            params.append(ast.literal_eval(arg))
        print(equalStacks(*params))
    except Exception as e:
        print(f"Please make sure all the params are okay, an error occured: \n\t {e}")

    # print(equalStacks([1, 1, 1, 2, 3], [2, 3, 4], [1, 4, 1, 1]))
    # print(equalStacks([1, 1, 4, 2, 3], [3, 3, 4], [1, 4, 1, 1]))
    # print(equalStacks([1, 1], [1, 3, 4], [1, 7, 1, 1]))
    # print(equalStacks([5, 7, 3], [1, 10, 1, 4, 4, 4, 4], [12]))
