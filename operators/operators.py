def operators(a, b):
    if 1 <= a <= 10**10 and 1 <= b <= 10**10:
        return "{}\n{}\n{}".format((a+b), (a-b), (a*b))


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(operators(a, b))
