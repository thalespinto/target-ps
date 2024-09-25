
def is_fib_member(n):
    n1 = 0
    n2 = 1
    while ((n1 + n2) < n):
        n1, n2 = n2, n1 + n2

    if  (n1 + n2) == n:
        print('Pertence a sequencia')
        return

    print('Não pertence a sequência')


def main():
    n = int(input('Insira o número a ser testado: '))
    is_fib_member(n)

if __name__ == "__main__":
    main()