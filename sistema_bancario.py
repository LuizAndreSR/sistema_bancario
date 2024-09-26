saldo = 0.00
valor_limite_saque = 500.00
extrato = []
quantidade_limite_saques= 3
numero_saques = 0
menu = """
***************************************************************
            Selecione uma opção para continuar.

                [1] Depositar
                [2] Sacar
                [3] Extrato
                [4] Sair

***************************************************************
"""

print(
    """

************** Bem vindo ao Banco do Luiz! ********************
    """
    )
while True:
    opcao_escolhida = input(f"{menu}=> ")

    if opcao_escolhida == "1":
        deposito = float(input("Digite o valor para deposito:\n=>"))
        if deposito > 0:
            saldo += deposito
            extrato.append(f"Deposito: R$ {deposito:,.2f}")
            print(f"Deposito no valor de R${deposito:,.2f} realizado com sucesso!\n")
        else:
            print("O valor de deposito deve ser maior que R$0,00.")
  
    elif opcao_escolhida == "2":
        saque = float(input("Digite o valor para saque:\n=>"))
        if numero_saques >= quantidade_limite_saques:
            print("Quantidade de saques excedida.")
        elif saque > valor_limite_saque:
            print("O valor informado excede o limite de saque da sua conta. Operação cancelada.\n")
            
        elif saque > saldo:
            print("Saldo insuficiente. Operação cancelada.\n")
            
        elif saldo > 0:
            saldo -= saque
            extrato.append(f"Saque: -{float(saque):,.2f}")
            numero_saques += 1
            print(f"Saque no valor de R${saque:,.2f} realizado com sucesso!\n")
        else:
            print("O valor de saque deve ser maior que R$0,00\n")

    elif opcao_escolhida == "3":
        print("*********** Extrato ***********\n")
        for x in range(len(extrato)):
            print(extrato[x])
        print(f"\nSaldo total: R${saldo:,.2f}\n")
        print("*******************************")
        

    elif opcao_escolhida == "4":
        print("O banco do Luiz agradece!")
        break

    else:
        print("Opção inválida, por favor, selecione novamente a operação desejada.")