"""
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once
"""


def print_all_possible_strings(lst):
    i = 0
    while i < len(lst):
        j = i+1
        while j < len(lst):
            lst[i], lst[j] = lst[j], lst[i]
            print(list.__str__(lst))
            j += 1
        i = i+1


"""
can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2
"""
def count_to_be_2(n):
    i = 0
    while n>=2:
        n = int(n)/2
        i+=1
    return i

def main():
    #lst = ['c', 'a', 't', 'd', 'o', 'g']
    #print_all_possible_strings(lst)
    print(count_to_be_2(8))


if __name__ == '__main__':
    main()
