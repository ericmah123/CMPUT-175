from importlib import invalidate_caches
from importlib import import_module
from os.path import exists
from os import remove
from random import randrange


def write_py(file_name, string_parameter, file_contents):
    """
    This is function takes the name of the file, the parameter that will be passed into the functions and finally the actual contents. A .py program will be produced
    """
    assert file_name != 'a3'
    file_name_mod = file_name + '.py'
    param_index = 0
    param_list = []
    while param_index < len(string_parameter):
        # This while loop is made to handle multiple parameters that are passed through. While loop ends when all parameters are appended together and joined with ","
        param_list.append(string_parameter[param_index])
        param_index += 1
        final_string = ', '.join(param_list)
    with open(file_name_mod, 'w') as file1:
        # opens up a new file in writing mode
        file1.write('def ' + file_name + f'({final_string}):')
        file1.write('\n')
        for i in range(0, len(file_contents)):
            # going through each index of file contents list and writing them to the new .py file
            file1.write('\t' + file_contents[i] + '\n')


def load_function(name):
    # invalidate_caches is necessary to import any files created after this file started!
    invalidate_caches()
    print(f"    Attempting to import {name}...")
    module = import_module(name)
    print(f"    Imported!")
    assert hasattr(module, name), f"{name} is missing from {name}.py"
    function = getattr(module, name)
    assert type(function) is type(load_function)
    return function


def fixed_bubble(num):
    """
   Writes a bubble sorting program using write_py
    """
    statement_list = []
    for i in range(0, num):
        for j in range(0, num - i - 1):
            # Bubble sorting for loops that are used to pass through sorting steps into what is being appended
            statement_list.append(f"if a_list[{j}] > a_list[{j + 1}]:")
            statement_list.append(f"\ta_list[{j}], a_list[{j + 1}] = a_list[{j + 1}], a_list[{j}]")
    statement_list.append('return a_list')
    write_py(f'bubble{num}', ['a_list'], statement_list)
    # Creating the .py program and passing final statement list into the third parameter


def flip(sign):
    """
    Flips sign depending on user input
    """
    if sign == '>':
        return '<'
    elif sign == '<':
        return '>'


def greatest_power_of_two_less_than(n):
    """
    Takes a single argument, an integer >= 1. It should return the greatest power of two that’s less than that.
    """
    if n < 1:
        return 'Not valid'
    elif n == 2:
        return 1
    else:
        for number in range(n, 0, -1):
            # Counts down and checks that if 2 to the power of number is less than given argument we return that result. Otherwise keep looping.
            if (2 ** number) < n:
                return 2 ** number


def bitonic_sort(a_list, start, end, direction):
    """
    Bitonic sort will sort part of the lists in the wrong order (descending instead of ascending) before merging it into the correct order
    """
    if (end - start) <= 1:
        return
    middle = (end + start) // 2
    # As the function is recursively called middle will continue to be called until the base case is hit which will then trigger the next recursive call
    # Once that is complete merge will be called
    bitonic_sort(a_list, start, middle, direction)
    bitonic_sort(a_list, middle, end, flip(direction))
    bitonic_merge(a_list, start, end, direction)


def bitonic_merge(a_list, start, end, direction):
    """
    This function like sort keeps track of indices and will perform comparing in swapping
    """
    if (end - start) <= 1:
        return
    distance = greatest_power_of_two_less_than(end - start)
    middle = end - distance
    for index in range(start, middle):
        # This chunk of code will compare and swap
        if direction == '>' and a_list[index] > a_list[index + distance]:
            a_list[index], a_list[index + distance] = a_list[index + distance], a_list[index]
        elif direction == '<' and a_list[index] < a_list[index + distance]:
            a_list[index], a_list[index + distance] = a_list[index + distance], a_list[index]
    bitonic_merge(a_list, start, middle, direction)
    bitonic_merge(a_list, middle, end, direction)


def bitonic(a_list):
    """
    Calls bitonic_sort and passes in required parameters
    """
    bitonic_sort(a_list, 0, len(a_list), '>')


def fixed_bitonic_sort(start, end, direction, my_list=None):
    """
    Very similar to original bitonic sort but the only difference is we have an optional parameter that will allow functionality in the complimentary function
    """
    if (end - start) <= 1:
        return
    middle = (end + start) // 2
    fixed_bitonic_sort(start, middle, direction, my_list)
    fixed_bitonic_sort(middle, end, flip(direction), my_list)
    fixed_bitonic_merge(start, end, direction, my_list)


def fixed_bitonic_merge(start, end, direction, my_list=None):
    """
    Very similar to bitonic sort but we have an optional parameter that allows us to append to a list
    """
    if (end - start) <= 1:
        return
    distance = greatest_power_of_two_less_than(end - start)
    middle = end - distance
    for index in range(start, middle):
        # Instead of comparing and swapping we will append to our parameter my_list, passing in the proper indexes that would mimic the process of a bitonic sort
        my_list.append(f"if a_list[{index}] {direction} a_list[{index + distance}]:")
        my_list.append(f"\ta_list[{index}], a_list[{index + distance}] = a_list[{index + distance}], a_list[{index}]")
    fixed_bitonic_merge(start, middle, direction, my_list)
    fixed_bitonic_merge(middle, end, direction, my_list)


def fixed_bitonic(size):
    """
    Takes in an integer that is a solely a size of a list and finishes the rest of the sorting
    """
    my_list = []
    fixed_bitonic_sort(0, size, '>', my_list)
    # Passes list into fixed bitonic sort to have contents passed into my_list
    my_list.append('return a_list')
    write_py(f'bitonic{size}', ['a_list'], my_list)


def main():
    write_py("add", ["a", "b"], ["r = a + b", "return r"])
    add = load_function("add")
    assert add(1, 2) == 3
    write_py("exponent", ["a", "b"], ['x = a ** b', 'return x'])
    exponent = load_function('exponent')
    assert exponent(3, 2) == 9
    write_py('name_age', ["name", "age"], ["x = f'my name is {name} and I am {age} years old!'", "return x"])
    name_age = load_function('name_age')
    assert name_age('Bill', 20) == 'my name is Bill and I am 20 years old!'


if __name__ == '__main__':
    main()
