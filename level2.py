
def formula(num):
    import math
    return int ( math.floor ( math.sqrt((2* 50 * num)/30) ))

    
def ex6(input_list):
    """
    Question:
    Write a program that calculates and prints the value 
    according to the given formula:
        Q = Square root of [(2 * C * D)/H]
        Following are the fixed values of C and H:
            C is 50. H is 30.
        D is the variable whose values should be input to your program
        in a comma-separated sequence.
    Example
    Let us assume
    the following comma separated input sequence is given to the program:
    100,150,180
    The output of the program should be:
    18,22,24
    """
    return [formula(i) for i in input_list]
    #return formula(100)
    

def ex7(X, Y):
    """
    Write a program which takes 2 digits, X,Y as input 
        and generates a 2-dimensional array. 
    The element value in the i-th row and j-th column of the array should be i*j.
    Note: i=0,1.., X-1; j=0,1.., Y-1.
    Example
    Suppose the following inputs are given to the program:
    3,5
    Then, the output of the program should be:
    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
    """
    m  = []
    for i in range(0, X):
        l = []
        for j in range(0, Y):
            l.append(i*j)
        m.append(l)
    return m


def ex8():
    """
    Question:
    Write a program that accepts a comma separated sequence of words as input 
    and prints the words in a comma-separated sequence 
    after sorting them alphabetically.
    
    Suppose the following input is supplied to the program:
        without,hello,bag,world
    Then, the output should be:
        bag,hello,without,world
    
    Hints:
    In case of input data being supplied to the question,
    it should be assumed to be a console input.
    """
    # print ",".join([x for x in raw_input('>>').split(',')].sort())
    input_str = raw_input('input comma seperated strings>')
    input_list = input_str.split(',')
    input_list.sort()
    print ",".join(input_list)

    
def ex9():
    """Write a program that accepts sequence of lines as input
    and prints the lines after making all characters in the sentence capitalized.
    Suppose the following input is supplied to the program:
        Hello world
        Practice makes perfect
    Then, the output should be:
        HELLO WORLD
        PRACTICE MAKES PERFECT
    """
    print 'Enter lines>>\n'
    lines = []
    while True:
        line = raw_input()
        if line == 'exit':
            break
        else:
            lines.append(line.upper())
        
    print "\n".join(lines)
    
    
def ex10():
    """
    Question:
    Write a program that accepts 
        a sequence of whitespace separated words as input 
        and prints the words after removing all duplicate words
        and sorting them alphanumerically.
    
    Suppose the following input is supplied to the program:
        hello world and practice makes perfect and hello world again
    Then, the output should be:
        again and hello makes perfect practice world

    Hints:
    In case of input data being supplied to the question, 
        it should be assumed to be a console input.
    We use set container to remove duplicated data automatically
    and then use sorted() to sort the data.
    """
    
    input_list = raw_input('Enter sequence of whitespace separated words as input>').split(' ')
    print " ".join (sorted(list(set(input_list))))

    
def ex11():
    """
    Question:
    Write a program which accepts a 
        sequence of comma separated 4 digit binary numbers as its input
        and then check whether they are divisible by 5 or not.
        The numbers that are divisible by 5 are to be printed in a comma separated sequence.
    Example:
        0100,0011,1010,1001
    Then the output should be:
     0100,1010
    Notes: Assume the data is input by console.
    Hints:
    In case of input data being supplied to the question, it should be assumed to be a console input.
    """
    print ",".join([ x for x in raw_input('>').split(',') if int(x) % 5 == 0 ])


def ex12():
    """
    Question:
    Write a program, which will find all such numbers 
    between 1000 and 3000 (both included) 
    such that each digit of the number is an even number.
    The numbers obtained should be printed in a comma-separated sequence
    on a single line.

    Hints:
    In case of input data being supplied to the question, 
    it should be assumed to be a console input.
    """
    print ",".join([str(x) for x in range(999,3001) if x%2 ==0 ]) 

  
def ex13(input_str):
    """
    Question:
    Write a program that accepts a sentence and 
    calculate the number of letters and digits.
    
    Suppose the following input is supplied to the program:
        hello world! 123
    Then, the output should be:
        LETTERS 10
        DIGITS 3
    """
    lc =0
    dc =0
    for c in input_str:
        if c.isalpha():
            lc+=1
        elif c.isdigit():
            dc+=1
    print "LETTERS %d" % lc
    print "DIGITS %d" % dc

            
def ex14(input_str):
    """
    Question:
    Write a program that accepts a sentence 
    and calculate the number of upper case letters and lower case letters.
    
    Suppose the following input is supplied to the program:
        Hello world!
    Then, the output should be:
    UPPER CASE 1
    LOWER CASE 9
    """
    uc = lc = 0
    for c in input_str:
        if c.isupper():
            uc+=1
        elif c.islower():
            lc+=1
    print "UPPER CASE %d" % uc
    print "LOWER CASE %d" % lc

    
def ex15(input_num):
    """
    Question:
    Write a program that computes the value of 
        a+aa+aaa+aaaa with a given digit as the value of a.
    Suppose the following input is supplied to the program:
    9
    Then, the output should be:
    11106
    """
    count = 0
    for i in range(1,5): 
        num = ""
        for j in range(i):
            num += str(input_num)
        count += int(num)
    print count


def ex16():
    """
    Use a list comprehension to square each odd number in a list.
    The list is input by a sequence of comma-separated numbers.
    Suppose the following input is supplied to the program:
        1,2,3,4,5,6,7,8,9
    Then, the output should be:
        1,9,25,49,81
    """
    print ",".join([str(int(x)**2) for x in raw_input('input>').split(',') \
                                                            if int(x)%2 != 0 ])


def ex17():
    """
    Question:
    Write a program that computes the net amount of a bank account 
    based a transaction log from console input.
    The transaction log format is shown as following:
    D 100
    W 200
    D means deposit while W means withdrawal.
    
    Suppose the following input is supplied to the program:
        D 300
        D 300
        W 200
        D 100
    Then, the output should be:
        500
    """
    print "Input the log:\n"
    total_amount = 0
    while True:
        line = raw_input()
        if line == 'exit':
            print "Amount withstanding : %d" % total_amount
            break
        else:
            transaction, amount = line.split(' ')
            amount = int(amount)
            if transaction == 'D':
                total_amount += amount
            elif transaction == 'W':
                total_amount -= amount
        
        
    
if __name__ == '__main__':
    #print ex6([100, 150, 180])
    #print ex7(3,5)
    #ex8()
    #ex9()
    #ex10()
    #ex11()
    #ex12()
    #ex13('hello world! 123')
    #ex14('Hello world!')
    #ex15(9)
    #ex16()
    ex17()
    