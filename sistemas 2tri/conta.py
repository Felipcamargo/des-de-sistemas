class Conta:
    def __init__(self, agencia, num, titular, saldo, senha):
        self.__agencia = agencia
        self.__num = num
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha

    @property
    def numero (self):
        return self.__num

    def extrato(self):
        return self.__saldo

    def sacar(self, valor):
        if valor < 0 or valor > self.__saldo:
            return False
        else:
            self.__saldo -= valor
            return True     

    def depositar(self, valor):
        if valor < 0:
            return False
        else:    
            self.__saldo += valor
            return True 

    def entrar(self, con, sen):
        if con != self.__num:
            return False
        else:
            if sen != self.__senha:
                return False
            else:
                return True        

    def transferir(self, valor, conta):
        if valor < 0 or valor > self.__saldo:
            return False    
        else:
            self.__saldo -= valor
            conta.depositar(valor)
            return True
     