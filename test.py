


def min_squares(m, n):
    if m == n:
        print("{} x {} ".format(m,m))
    elif m > n:
        print("{} x {} ".format(n,n))
        return min_squares(m-n,n)
    else:
        print("{} x {} ".format(m,m))
        return min_squares(n-m,m)

# Example usage:
# result = min_squares(11, 13)


test = set((1,2,3,4))
if 10 not in test:
    print("no 10")