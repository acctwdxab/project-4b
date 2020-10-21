# Dan Wu
# 10/19/2020
# To create a function that takes a positive integer parameter and returns the number at that position of the Fibonacci sequence.

def fib(num):
    """The fib function returns the positive number at the position of the fibonacci sequence."""

    first_num, second_num = 0 , 1
    for i in range ( num ) :
        first_num , second_num = second_num , first_num + second_num
    return first_num

