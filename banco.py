saldo=1000

def depositar(valor):
    global saldo
    saldo+=valor
    return saldo

def sacar(valor):
    global saldo
    saldo-=valor
    return saldo

def extrato():
    global saldo
    print(f"Seu saldo é R${saldo}")

while True:
    print("***** Bem-vindo(a) ao Banco Mais Você *****")
    print("Digite 1 - Saque")
    print("Digite 2 - Depósito")
    print("Digite 3 - Verificar o extrato")
    print("Digite 0 - Encerrar a operação")
    op = int(input("Informe a operação desejada:"))
    print()

    if op==1:
        valor=float(input("Informe o valor do saque:"))
        if valor<=0 or valor > saldo:
            print("Saque inválido")
            print()
            continue
        else:
            sacar(valor)
            print("Saque realizado com sucesso!!!")
            print()
    elif op==2:
        valor=float(input("Informe o valor do deposito:"))
        if valor<=0:
            print("Depósito inválido")
            print()
            continue
        else:
            depositar(valor)
            print("Deposito realizado com sucesso!!!")
            print()
    elif op==3:
        extrato()
        print()
    elif op==0:
        print("Fim da operação")
        print("Banco Mais deseja-te um ótimo dia")
        break
    else:
        print("Opção Inválida!!!")
        print()
