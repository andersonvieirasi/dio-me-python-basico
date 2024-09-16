from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
clientes=[]
class Cliente:
    def __init__(self, endereco):
        self.endereco=endereco
        self.contas=[]

    def realizarTransacao(self,conta):
        transacao.registrar(conta)

    def adicionarConta(self, conta):
        self.contas.append(conta)

class PF(Cliente):
    def __init__(self, nome, data_nasc, cpf, endereco):
        super().__init__(endereco)
        self.nome=nome
        self.data_nasc=data_nasc
        self.cpf=cpf
    
    def adicionar_cliente(self, cli):
        clientes.append(cli)
        

class Conta:
    def __init__(self, numero, cliente):
        self._saldo=0
        self._numero=numero
        self._agencia="1234-5"
        self._cliente=cliente
        self._historico=Historico()
    
    @classmethod
    def contaNova(cls,cliente,numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self,valor):
        if valor>self._saldo:
            print("ATENÇÃO: Saldo Insuficiente!!!")
            return False
        elif valor>0:
            self._saldo-=valor
            print("Saque realizado com sucesso.")
            return True
        else:
            print("ATENÇÃO: O valor inserido é inválido")
        return False
    
    def depositar(self, valor):
        if valor <=0:
            print("ATENÇÃO: o Valor inserido é inválido.")
            return False
        else:
            self._saldo+=valor
            print("Depósito realizado com sucesso.")
            return True

class CC(Conta):
    def __init__(self, numero, cliente, limite=1000, qtde_saque=3):
        super().__init__(numero, cliente)
        self.limite=limite
        self.qtde_saque=qtde_saque

    def sacar(self,valor):
        num_saques=len([transacao for transacao in 
                        self.historico.transacoes if transacao["tipo"]=="Saque"])
        if valor>self.limite:
            print("Limite de saque diário excedido, retorne amanhã...")
        elif valor<=0 or valor > self.saldo: 
            print("O valor inserido é inválido...")
        else:
            super().sacar(valor)

        def __str__(self):
            texto = f"Agência: {self.agencia}\nC/C: {self.numero}\nTitular: {self.cliente.nome} "
            return texto


class Historico:
    def __init__(self):
        self._transacoes=[]

    @property
    def transacoes(self):
        return self._transacoes
    
    def adiocionar_transacao(self,transacao):
        {
            "tipo": transacao.__class__.__name__,
            "valor":transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y"),
            "hora": datetime.now().strftime("%H:%M:%s"),
        }

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor=valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao=conta.sacar(self._valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    
    def __init__(self, valor):
        self._valor=valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao=conta.depositar(self._valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)



def criar_usuario():
    cpf=input("Informe o cpf:")
    if verificar(cpf):
        nome=input("Informe o nome:")
        data_nasc=input("Informe sua data de nascimento (modelo: 01/01/1980):")
        endereco=input("Informe seu endereço:")
        usuario = PF(nome, data_nasc, cpf, endereco)
        usuario.adicionar_cliente(usuario)
        print("Cliente cadastrado com sucesso!!!")   
        print()  
    else:
        print("Cliente já possui cadastro neste banco.") 
        print()
  

def abrir_conta():
    cpf = input("Informe o CPF do cliente:")
    cliente =  next((cli for cli in clientes if cli.cpf == cpf), None)    
    if cliente:
        numero = input("Informe o número da conta:")
        tipo_conta = input("Informe o tipo de conta (CC para Conta Corrente):").strip().upper()
        
        if tipo_conta == "CC":
            limite = float(input("Informe o limite da conta corrente:"))
            qtde_saque = int(input("Informe a quantidade de saques permitidos por dia:"))
            conta = CC(numero, cliente, limite, qtde_saque)
        else:
            print("Tipo de conta inválido.")
            return
        cliente.adicionarConta(conta)
        print("Conta criada com sucesso!")
        5
    else:
        print("Cliente não encontrado.")

    

def verificar(cpf):
    global clientes
    for cliente in clientes:
        if cliente.cpf==cpf:
                return False
    else:
        return True
   
def depositar():
    cpf = input("Informe o CPF do cliente:")
    cliente = next((cli for cli in clientes if cli.cpf == cpf), None)
    
    if cliente:
        numero_conta = input("Informe o número da conta:")
        conta = next((c for c in cliente.contas if c.numero == numero_conta), None)
        
        if conta:
            valor = float(input("Informe o valor do depósito:"))
            if isinstance(conta, Conta):
                conta.depositar(valor)  # Corrigido para passar o valor diretamente
            else:
                print("Tipo de conta não suportado para depósito.")
        else:
            print("Conta não encontrada.")
    else:
        print("Cliente não encontrado.")

def sacar():
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((cli for cli in clientes if cli.cpf == cpf), None)
    
    if cliente:
        numero_conta = input("Informe o número da conta: ")
        conta = next((c for c in cliente.contas if c.numero == numero_conta), None)
        
        if conta:
            valor = float(input("Informe o valor do saque: "))
            if isinstance(conta, Conta):
                sucesso_transacao = conta.sacar(valor)
                if sucesso_transacao:
                    transacao = Saque(valor)
                    conta.historico.adicionar_transacao(transacao)
            else:
                print("Tipo de conta não suportado para saque.")
        else:
            print("Conta não encontrada.")
    else:
        print("Cliente não encontrado.")


def extrato():
    cpf = input("Informe o CPF do cliente:")
    cliente = next((cli for cli in clientes if cli.cpf == cpf), None)
    
    if cliente:
        numero_conta = input("Informe o número da conta:")
        conta = next((c for c in cliente.contas if c.numero == numero_conta), None)
        
        if conta:
            print(f"Extrato da Conta {conta.numero}:")
            print(f"Saldo: R${conta.saldo:.2f}")
            print("Histórico de Transações:")
            for transacao in conta.historico.transacoes:
                print(f"{transacao['data']} {transacao['hora']} - {transacao['tipo']} - R${transacao['valor']:.2f}")
        else:
            print("Conta não encontrada.")
    else:
        print("Cliente não encontrado.")



def listar():
    if clientes:
        print("Clientes cadastrados:")
        for cliente in clientes:
            print(f'Nome: {cliente.nome}, CPF: {cliente.cpf}, Data de Nascimento: {cliente.data_nasc}, Endereço: {cliente.endereco}')
            if cliente.contas:
                print("Contas:")
                for conta in cliente.contas:
                    print(f"  - Número: {conta.numero}, Agência: {conta.agencia}, Tipo: {conta.__class__.__name__}")
            else:
                print("  Nenhuma conta cadastrada.")
    else:
        print("Nenhum cliente cadastrado.")


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
        sacar()
    elif op==4:
        depositar()
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
