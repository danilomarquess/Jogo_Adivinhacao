import random
import time

def jogar():
    print("\n*** Bem vindo ao Jogo da Adivinhação! ***")
    start = time.time()
    tentativas = int(input("Informe a quantidade de tentativas que você quer ter: "))
    numero_correto = random.randint(1, 20)
    print(f"Você escolheu ter {tentativas} tentativas")
    historico = []


    contador = 1

    while True:
        try:
            entrada = int(input("Digite um número de 1 a 20: "))
        except ValueError:
            print("Digite um número válido: ")
            continue
        historico.append(entrada)
        if entrada < 1 or entrada > 20:
            print("Você digitou um número fora do intervalo 1-20")
            continue
        if entrada == numero_correto:
            print(f"Parabéns! Você acertou o número {numero_correto}")
            print(f'Tentativas realizadas: {contador}')
            print(f'Histórico de Tentativas: {historico}')
            break
        if contador >= tentativas:
            print(f"Você esgotou todas as suas tentativas!")
            print(f'Histórico de Tentativas: {historico}')
            break
        
        if entrada > numero_correto:
            print(f'{entrada} é maior do que o número da sorte')
        else:
            print(f'{entrada} é menor do que o número da sorte')
        
        contador += 1

    print(f'Tempo gasto: {time.time() - start:.2f}')
while True:
    jogar()
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
    if jogar_novamente == 's':
        print("=====================================================")
    else:
        print("Obrigado por jogar! Até a próxima!")
        break
    


