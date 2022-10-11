import sys
import ast


def equalStacks_rec(h1: list, h2: list, h3: list):
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
    sorted_stacks = sorted([h1, h2, h3], key=sum, reverse=True)
    sorted_stacks[0].pop(0)
    height = sum(sorted_stacks[0])

    while sum(sorted_stacks[1]) > height:
        sorted_stacks[1].pop(0)

    while sum(sorted_stacks[2]) > height:
        sorted_stacks[2].pop(0)

    return equalStacks(*sorted_stacks)



def equalStacks(h1: list, h2: list, h3: list):
    """
    Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. 
    This means you must remove zero or more cylinders from the top of zero or more of the three stacks until
    they are all the same height, then return the height.

    assume the input is always correct
    """

    # return if result is achieved

    sorted_stacks = sorted([h1, h2, h3], key=sum, reverse=True)

    height_h1 = sum(sorted_stacks[0])
    height_h2 = sum(sorted_stacks[1])
    height_h3 = sum(sorted_stacks[2])

    while not (height_h1 == height_h2 and height_h2 == height_h3):
        height_h1 -= sorted_stacks[0].pop(0)

        while height_h2 > height_h1:
            height_h2 -= sorted_stacks[1].pop(0)

        while height_h3 > height_h1:
            height_h3 -= sorted_stacks[2].pop(0)
        
    return height_h1




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
    # print(equalStacks([1, 2, 1, 1], [1, 1, 2], [1,1])) # 2

    # print('\n')
    # print(equalStacks([3,2,1,1,1], [4,3,2], [1,1,4,1])) # 5

    # print('\n')
    # print(equalStacks([1, 1, 4, 2, 3], [3, 3, 4], [1, 4, 1, 1])) # 0

    # print('\n')
    # print(equalStacks([1, 1], [1, 3, 4], [1, 7, 1, 1])) #0

    # print('\n')
    # print(equalStacks([2, 7, 3], [1, 10, 1, 4, 4, 4, 4], [12])) #12
