from functools import total_ordering
#para funcionar o fator <= ou =>
@total_ordering
class Conta:
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 1000

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

    #definindo ordem natural:
    def __eq__(self, outro):
        if type(outro) != ContaCorrente:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo
 
    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo
        
class ContaCorrente(Conta):
    def passa_mes(self):
        self._saldo -= 3

class ContaPoupanca(Conta):
    def passa_mes(self):
        self._saldo += 3

conta1 = ContaCorrente(55)
conta2 = ContaCorrente(55)

b = conta1 == conta2
print(b)
