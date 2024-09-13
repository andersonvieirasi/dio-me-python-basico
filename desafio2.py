saldo=1000
agencia="0001"
numero_conta=10000
clientes=[]
cliente={}
contas=[]
conta=[]
qtde_saque=3

def criar_usuario():
    cpf=input("Informe o cpf:")
    if verificar(cpf):
        nome=input("Informe o nome:")
        data_nasc=input("Informe sua data de nascimento (modelo: 01/01/1980):")
        endereco=input("Informe seu endereço:")
        global cliente, clientes
        cliente={'cpf':cpf, 'nome':nome, 'data_nasc':data_nasc, 'endereco':endereco}
        clientes.append(cliente)
        print("Cliente cadastrado com sucesso!!!")   
        print()  
    else:
        print("Cliente já possui cadastro neste banco.") 
        print()
  

def abrir_conta():
    global agencia, numero_conta
    conta=+1
    tipo=input("Informe o tipo da conta:")
    cliente={"agencia":agencia, 'numero da conta':numero_conta, "tipo":tipo}
    clientes.append(cliente)

def verificar(cpf):
    global clientes,cliente
    for i in clientes:
        for j in cliente:
            if cliente["cpf"]==cpf:
                return False
    else:
        return True
    
    
def depositar(valor):
    
    if valor<=0:
        print("Depósito inválido")
        print()
    else:
        global saldo
        saldo+=valor
        print("Deposito realizado com sucesso!!!")
        print()
   

def sacar(valor):
    global qtde_saque
    global saldo
    if qtde_saque<1:
        print("Limite de saque diário excedido, retorne amanhã...")
        print()
    elif valor<=0 or valor > saldo: 
        print("Saque inválido")
        print()
    else:
        saldo-=valor
        qtde_saque-=1
        print("Hoje você tem mais",qtde_saque,"saque(s).")
        print("Saque realizado com sucesso!!!")
        print()
    
def extrato():
    global saldo
    print(f"Seu saldo é R${saldo:.2f}")

def listar():
    global clientes,cliente
    for i in clientes:
        print(f'Nome: {i["nome"]} , CPF: {i["cpf"]}, Data de Nascimento: {i["data_nasc"]}, Endereço: {i["endereco"]} ')


while True:
    print("***** Bem-vindo(a) ao Banco Mais Você *****")
    print("Digite 1 - Cadastar novo cliente")
    print("Digite 2 - Criar nova conta")
    print("Digite 3 - Saque")
    print("Digite 4 - Depósito")
    print("Digite 5 - Verificar o extrato")
    print("Digite 6 - Listar os clientes do banco")
    print("Digite 0 - Encerrar a operação")
    op = int(input("Informe a operação desejada:"))
    print()
    if op==1:
        criar_usuario()
    elif op==2:
        abrir_conta()
    elif op==3:
        valor=float(input("Informe o valor do saque:"))
        sacar(valor)
    elif op==4:
        valor=float(input("Informe o valor do deposito:"))
        depositar(valor)
    elif op==5:
        extrato()
        print()
    elif op==6:
        listar()
        print()
    elif op==0:
        print("Fim da operação")
        print("Banco Mais deseja-te um ótimo dia")
        break
    else:
        print("Opção Inválida!!!")
        print()
