#-*- coding: latin1 -*-
from errors import ValorInvalidoError
from errors import SaldoInsuficienteError


class Conta:

    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0
        self.extrato=[]

    def __str__(self):
        return " Conta " + str(self.numero) + "\n" + " Saldo R$" + str(self.saldo)

    def op_saldo(self) :
        return self.saldo

    def op_saque(self, valor) :
        if (valor > self.saldo) :
            raise SaldoInsuficienteError()
        elif (valor <= 0):
            raise ValorInvalidoError()
        else :
            self.saldo = self.saldo - valor
            self.extrato.append("/Saque/ ----------"+" R$: "+str(valor))
            if len(self.extrato) > 10:
            	del self.extrato[0]

    def op_deposito(self, valor) :
        if (valor <= 0):
            raise ValorInvalidoError()
        else :
            self.saldo = self.saldo + valor
            self.extrato.append("/Depósito/ -------"+" R$: "+str(valor))
            if len(self.extrato) > 10:
            	del self.extrato[0]

    def op_extrato(self):
    	exibir = "====================\n"+"Extrato – Conta: "+str(self.numero)+"\n====================\n"+"Ultimas 10 operações"+"\n====================\n"
    	for operacao in range(len(self.extrato)):
            exibir+=self.extrato[operacao]+"\n"
        exibir+="====================\n"+"Saldo: R$ "+str(self.saldo)
        return exibir

