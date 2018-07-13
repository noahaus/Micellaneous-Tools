#Combinatorics Calculator, just for fun

#### Functions

#In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5 ! = 5 × 4 × 3 × 2 × 1 = 120. 

def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        return "negative numbers cannot be used for factorials"
    else:
        result = num
        while True:
            num -= 1
            result = result*(num)
            if num == 1:
                break
        
        return result

#In mathematics, the notion of permutation relates to the act of arranging all the members of a set into some sequence or order, or if the set is already ordered, rearranging (reordering) its elements, a process called permuting. These differ from combinations, which are selections of some members of a set where order is disregarded.

def permutation(num,selection):
    return factorial(num)/factorial(num-selection)

#In mathematics, a combination is a selection of items from a collection, such that (unlike permutations) the order of selection does not matter. For example, given three fruits, say an apple, an orange and a pear, there are three combinations of two that can be drawn from this set: an apple and a pear; an apple and an orange; or a pear and an orange.
def combination(num,selection):
    return permutation(num,selection)/factorial(selection)
    
#### Free space to make as many computations as needed for combinatoric problems. 