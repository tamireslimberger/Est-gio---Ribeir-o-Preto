def gerar_fibonacci_ate_n(n):
    #Gera a sequência de Fibonacci até o número fornecido e retorna uma lista com os valores.
    fibonacci_seq = [0, 1]  # Inicia a sequência com os primeiros dois números
    while True:
        proximo = fibonacci_seq[-1] + fibonacci_seq[-2]
        if proximo > n:
            break
        fibonacci_seq.append(proximo)
    return fibonacci_seq

def pertence_a_fibonacci(n):
    #Verifica se um número pertence à sequência de Fibonacci gerada.
    fibonacci_seq = gerar_fibonacci_ate_n(n)
    return n in fibonacci_seq

def main():
    try:
        num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
        if pertence_a_fibonacci(num):
            print("O número {} pertence à sequência de Fibonacci.".format(num))
        else:
            print("O número {} NÃO pertence à sequência de Fibonacci.".format(num))
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()