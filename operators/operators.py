def operators(a, b):
    if a and b in range(1, 10**10):
        return '{}\n{}\n{}'.format((a+b), (a-b), (a*b))


if __name__ == '__main__':
    a, b = int(input()), int(input())
    print(operators(a, b))
