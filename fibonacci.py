def fibonacci(n):
    if n == 0 or n ==1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def run():

    n = int(input('Hola, ingresa un número para operar con la función fibonacci: '))
    print(fibonacci(n))


if __name__ == '__main__':
    run()