#  A) Sequência de números ímpares
sequencia = [1, 3, 5, 7]
proximo = sequencia[-1] + 2  # Adiciona 2 ao último elemento
print("Resposta a) Dada a sequência 1, 3, 5, 7, o próximo número é: {}.\n".format(proximo))
#Próximo Elemento: O próximo número ímpar após 7 é 9.

#B) Sequência de potências de 2
sequencia = [2, 4, 8, 16, 32, 64]
proximo = sequencia[-1] * 2  # Multiplica o último elemento por 2
print("Resposta b) Dada a sequência 2, 4, 8, 16, 32, 64, o próximo número é: {}.\n".format(proximo))
#Próximo Elemento: O próximo número é 64 * 2 = 128.

#C) Sequência dos quadrados dos números naturais
sequencia = [0, 1, 4, 9, 16, 25, 36]
indice = len(sequencia)  # Próximo índice é 7
proximo = indice ** 2  # Quadrado do próximo índice
print("Resposta c) Dada a sequência 0, 1, 4, 9, 16, 25, 36, o próximo número é: {}.\n".format(proximo))
#Próximo Elemento: O próximo número é 7^2 = 49.

#D) Sequência dos quadrados dos números pares
sequencia = [4, 16, 36, 64]
proximo = (len(sequencia) * 2 + 2) ** 2  # Quadrado do próximo número par
print("Resposta d) Dada a sequência 4, 16, 36, 64, o próximo número é: {}.\n".format(proximo))
#Próximo Elemento: O próximo número é 10^2 = 100.

#E) Sequência de Fibonacci
sequencia = [1, 1, 2, 3, 5, 8]
proximo = sequencia[-1] + sequencia[-2]  # Soma dos dois últimos números
print("Resposta e) Dada a sequência 1, 1, 2, 3, 5, 8, o próximo número é: {}.\n".format(proximo))
#Próximo Elemento: O próximo número é 5 + 8 = 13.

#F)Sequência observada
sequencia = [2, 10, 12, 16, 17, 18, 19]
proximo = sequencia[-1] + 1  # Adiciona 1 ao último número
print("Resposta f) Dada a sequência 2, 10, 12, 16, 17, 18, 19, o próximo número é: {}.".format(proximo))
#Próximo Elemento: O próximo número é 20.

