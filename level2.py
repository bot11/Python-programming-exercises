


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
    
    
if __name__ == '__main__':
    print ex6([100, 150, 180])