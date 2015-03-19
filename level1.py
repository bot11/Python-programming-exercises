

def ex1():
    """#Write a program which will find all such numbers which are 
        divisible by 7 but are not a multiple of 5,
        between 2000 and 3200 (both included).
        The numbers obtained should be printed in a 
        comma-separated sequence on a single line."""
    outstr = ""
    for num in range(2000, 3201):
        if num % 7 == 0 and num % 5 != 0:
            if outstr is "":
                outstr = "%s" % num
            else:
                outstr = outstr+",%s" % num
    return outstr

def factorial(num):
    fact = num
    while num > 1:
        fact = fact * (num -1)
        num = num - 1
    return fact
    
def ex2(inputlist):
    """Write a program which can compute the factorial of a given numbers.
    The results should be printed in a 
    comma-separated sequence on a single line.
    Suppose the following input is supplied to the program:
    8
    Then, the output should be:
    40320"""
    outputlist = [ factorial(num) for num in inputlist ] # <--List comprehension
    # outputlist = []
    # for num in listofnum:
    #     output = factorial(num)
    #     outputlist.append(output)
    return outputlist

def ex3(num):
    """With a given integral number n, 
    write a program to generate a dictionary that contains (i, i*i) 
    such that is an integral number between 1 and n (both included). 
    and then the program should print the dictionary.
    Suppose the following input is supplied to the program:
    8
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""
    
    dict = {i: i*i for i in range(1, num+1)}# <- Dictionary comprehension
    # dict = {}
    # for i in range(1, num+1):
    #     dict[i] = i*i     
    return dict

def ex4():
    """Write a program which accepts a sequence of comma-separated numbers
    from console and generate a list and a tuple which contains every number.
    Suppose the following input is supplied to the program:
    34,67,55,33,12,98
    Then, the output should be:
    ['34', '67', '55', '33', '12', '98']
    ('34', '67', '55', '33', '12', '98')"""
    print raw_input().split(',')
    print tuple(raw_input().split(','))
  
if __name__ == '__main__':
    #print ex2([1, 2, 3])
    #print ex3(8)
    ex4()