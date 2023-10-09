import os
import time
menu = """
                   
                       BANCO DIGITAL
  
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("========".center(60,"="),end=" ")
    opcao = input(menu)

    if opcao == "d":
        os.system("cls")
        print("Depósito".center(60,"="))
        print()

        deposito = float(input("Digite o valor que será o valor depositado:  "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("Depósito concluido com sucesso! seu saldo foi atualizado.")

        else:
            print("Não é possivel depositar este valor! tente novamente.")
        
        print()
        print("========".center(60,"="))
        print("Voltando para o menu...")
        time.sleep(3)
        os.system("cls")

    elif opcao == "s":
        os.system("cls")
        print("Saque".center(60,"="))

        if numero_saques < LIMITE_SAQUES:
            valor_sacado = float(input("Digite o valor que será sacado: "))
            excedeu_saldo = valor_sacado > saldo
            excedeu_limite = valor_sacado > 500

            if excedeu_saldo:
                print("Não será possivel sacar por falta de saldo!")

            elif excedeu_limite:
                print("Operação falhou! o valor do saque excede o limite")       

            elif valor_sacado > 0: 
                extrato += f"Saque: R$ {valor_sacado:.2f}\n"
                numero_saques += 1
                saldo -= valor_sacado
                print("Valor sacado com sucesso!")

            else:
                print("Operação falhou! o valor informado é inválido.")

        else:
            print("Você ultrapassou o limite de saques diários!")

        print("========".center(60,"="))
        print("Voltando para o menu...")
        time.sleep(3)
        os.system("cls")

    elif opcao == "e":
        os.system("cls")
        print("Extrato".center(60,"="))
        print()
        print("Não foram realizadas movimentações!" if not extrato else extrato)
        print(f"Saldo: R$ {saldo}")
        print("========".center(60,"="))
        print("Voltando para o menu...")
        time.sleep(5)
        os.system("cls")
        
    elif opcao == "q":
        break
   
    else:
        os.system("cls")
        print("Operação inválida, por favor selecione novamente a operação desejada")
