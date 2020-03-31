# Reinforcements exercieses
"""
takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
"""


def is_multiple(n, m):
    x = n % m
    print(x)
    return True if x == 0 else False


def main():
    n = int(input('enter n : '))
    m = int(input('enter m : '))
    print(is_multiple(n, m))
    while True :
        pass
        try:
            input('enter an input or Ctrl+D')
        except EOFError :
            break
    print('\n .. hello .. ')    


if __name__ == '__main__':
    main()
