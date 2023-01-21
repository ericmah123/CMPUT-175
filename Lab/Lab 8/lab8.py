def mylen(some_list):

    if some_list == []:
        return 0
    else:
        return 1 + mylen(some_list[:-1])



def intDivision(dividend, divisor):

    if dividend < 0 and divisor < 0:
        raise Exception('Cannot be negative number')
    if divisor == 0:
        raise Exception('Divisor cannot be 0')

    if dividend < divisor:
        return 0
    else:
        return 1 + intDivision(dividend - divisor, divisor)


def sumdigits(number):
    if number < 0:
        raise Exception('No negative numbers')
    if number == 0:
        return 0
    else:
        return (number % 10) + sumdigits(number // 10)


def reverseDisplay(number):
    if number < 0:
        raise Exception('No negative numbers!')

    if number > 0:

        print(number % 10, end='')
        return reverseDisplay(number//10)



def binary_search2(key, alist, low, high):

    if high >= low:


        guess = (high + low)//2

        if key == alist[guess]:
            return guess
        elif key < alist[guess]:
            return binary_search2(key, alist, low, guess - 1)

        else:
            return binary_search2(key, alist, guess + 1, high)

    else:
        return 'Item is not in list'


def main():
    alist = [43, 76, 97, 86]
    print(mylen(alist))


    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    print(intDivision(n, m))

    number = int(input('Enter a number:'))
    print(sumdigits(number))

    number = int(input('Enter a number:'))
    reverseDisplay(number)

    some_list = [-8,-2,1,3,5,7,9]

    print(binary_search2(9,some_list,0,len(some_list)-1))
    print(binary_search2(-8,some_list,0,len(some_list)-1))
    print(binary_search2(4,some_list,0,len(some_list)-1))


main()
