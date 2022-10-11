import sys
import ast


def equalStacks(h1: list, h2: list, h3: list):
    """
    Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. 
    This means you must remove zero or more cylinders from the top of zero or more of the three stacks until
    they are all the same height, then return the height.

    assume the input is always correct
    """

    # return if result is achieved
    height = sum(h1)
    if height == sum(h2) and height == sum(h3):
        return height

    # sort stacks by height and remove the 1st pizza
    sorted_stacks = sorted([h1,h2,h3], key=sum, reverse=True)
    print("pop elemnt from 0:", sorted_stacks[0].pop(0))
    height = sum(sorted_stacks[0])

    while sum(sorted_stacks[1]) > height:
        print(f"stack 1:{sorted_stacks[1]}")
        print("pop elemnt:", sorted_stacks[1].pop(0))

    while sum(sorted_stacks[2]) > height:
        print(f"stack 2:{sorted_stacks[1]}")
        print("pop elemnt:", sorted_stacks[2].pop(0))

    return equalStacks(*sorted_stacks)


if __name__ == "__main__":

    try:
        params = []
        for arg in sys.argv[1:]:
            params.append(ast.literal_eval(arg))
        print(equalStacks(*params))
    except Exception as e:
        print(
            f"Please make sure all the params are okay, an error occured: \n\t {e}")

    # DEBUG
    # params = []
    # for arg in sys.argv[1:]:
    #     params.append(ast.literal_eval(arg))
    # print(equalStacks(*params))

    # print('\n')
    # print(equalStacks([3,2,1,1,1], [4,3,2], [1,1,4,1])) # 5

    # print('\n')
    # print(equalStacks([1, 1, 4, 2, 3], [3, 3, 4], [1, 4, 1, 1])) # 0

    # print('\n')
    # print(equalStacks([1, 1], [1, 3, 4], [1, 7, 1, 1])) #0

    # print('\n')
    # print(equalStacks([2, 7, 3], [1, 10, 1, 4, 4, 4, 4], [12])) 
