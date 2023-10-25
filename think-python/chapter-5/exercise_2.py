def check_fernat(a, b, c, n):
    if n > 2:
        if a**n + b**n == c**n:
            print("Holy smokes, Fernat was wrong!")
        else:
            print("No, that does not work!")
    else:
        print("'n' must be greater than 2!")

check_fernat(54,67,54,2)