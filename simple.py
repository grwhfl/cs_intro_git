
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def main():
    print fib(10)
    a=fib(9)
    print(a**100 % 10**9+7)


if __name__ == "__main__":
    main()