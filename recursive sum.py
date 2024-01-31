#calculate the sum of numbers from 1 to n using recursion.
def recursivesum(first, last):
    temp = first
    if first == last:
        return temp
    else:
        return temp+recursivesum(first+1,last)

print(recursivesum(1,5))
