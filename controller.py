#coding:latin1
from errors import ValorInvalidoError
from errors import SaldoInsuficienteError
from Tkinter import *
from conta import Conta

class Controller:

    def __init__(self):
        self.contas = {}

    def saque(self,nConta,valor,feddBackLabel):

            if self.contas.has_key(nConta):
                conta=self.contas[nConta]
            else:
                feddBackLabel["text"]="Conta invalida!"
            try:
                conta.op_saque(float(valor))
                feddBackLabel["text"]="Saque realizado com sucesso!"
            except ValorInvalidoError as vie:
                feddBackLabel["text"]=vie
            except SaldoInsuficienteError as sie:
                feddBackLabel["text"]=sie

    def deposito(self,nConta,valor,feddBackLabel):

        if self.contas.has_key(nConta):
    		conta=self.contas[nConta]
    		try:
    			conta.op_deposito(float(valor))
    			feddBackLabel["text"]="Deposito realizado com sucesso!"
    		except ValorInvalidoError as vie:
    			feddBackLabel["text"]=vie
    	else:
    		feddBackLabel["text"]="Conta inexistente!"
    
    def cadastro(self,nConta,feedBackLabel):
        
        if self.contas.has_key(nConta) :
            feedBackLabel["text"]="Conta já cadastrada!"
        else:
            conta = Conta(nConta)
            self.contas[nConta] = conta
            feedBackLabel["text"]="Conta cadastrada com sucesso!"

    def extrato(self,nConta,feedBackLabel):

        if self.contas.has_key(nConta) :
            feedBackLabel["text"]=self.contas[nConta].op_extrato()
        else:
            feedBackLabel["text"]="Conta inexistente!"

    def saldo(self,nConta,feedBackLabel):

        if self.contas.has_key(nConta) :
            feedBackLabel["text"]=self.contas[nConta]
        else:
            feedBackLabel["text"]="Conta inexistente!"