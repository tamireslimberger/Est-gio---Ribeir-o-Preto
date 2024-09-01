def contar_letra_a(s):
   #Conta a quantidade de vezes que a letra 'a' (maiúscula ou minúscula) aparece em uma string.
    # Converte a string para minúsculas para garantir que 'A' e 'a' sejam tratados da mesma forma
    s = s.lower()
    quantidade = s.count('a')
    return quantidade

def main():
    texto = input("Digite uma string para verificar a quantidade de letras 'a': ")
    quantidade = contar_letra_a(texto)
    print("A letra 'a' (maiúscula ou minúscula) aparece {} vez(es) na string.".format(quantidade))

if __name__ == "__main__":
    main()