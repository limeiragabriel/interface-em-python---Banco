#coding:latin1
from errors import ValorInvalidoError
from errors import SaldoInsuficienteError
from Tkinter import *
from controller import Controller


controlador = Controller()

class Set_Gui:

    def __init__(self):

    	#=============janela principal=================================================
        mainWindow =Tk()
        mainWindow.title('/-/ Banco /-/') #=============titulo=========================
        #==============================================================================
        #=========================descricao das opeacoes===============================
        descricao=Label(mainWindow,text="Operações em conta:")
        descricao.place(x=60,y=8)
        #==============================================================================
        #================================botoes========================================
        btCadastro = Button(mainWindow,text="Cadastrar",width=20, command=self.cadastro)
        btSaldo = Button(mainWindow,text="Consutar Saldo",width=20, command=self.saldo)
        btSaque = Button(mainWindow,text="Saque",width=20, command=self.saque)
        btDeposito = Button(mainWindow,text="Deposito",width=20, command=self.deposito)
        btExtrato = Button(mainWindow,text="Extrato",width=20, command=self.extrato)
        #==============================================================================
        #==============================posicionamento==================================
        btCadastro.place(x=60,y=30)
        btSaldo.place(x=60,y=60)
        btSaque.place(x=60,y=90)
        btDeposito.place(x=60,y=120)
        btExtrato.place(x=60,y=150)
        #==============================================================================
        #=========================loop da janela e size================================
        mainWindow.geometry("300x200+300+200")
        mainWindow.mainloop()
        #==============================================================================
    
    #===================================janela cadastro================================
    def cadastro(self):

    		#=================================janela===================================
            Window =Tk()
            Window.title('/-/ Banco /-/') #================titulo======================
            #==========================================================================
            #============================== widgets ===================================
            descricao=Label(Window,text="Digite o número da conta:")
            entrada=Entry(Window,width=23)
            okButton=Button(Window,text="OK",width=20, command=lambda:controlador.cadastro(entrada.get(),feedbackLabel))
            feedbackLabel=Label(Window,text="")
            #==========================================================================
            #==========================posicionamento==================================
            descricao.place(x=60,y=10)
            entrada.place(x=60,y=40)
            okButton.place(x=60,y=80)
            feedbackLabel.place(x=60,y=150)
            #==========================================================================
            #=========================== loop e size===================================
            Window.geometry("300x200+400+200")
            Window.mainloop()
            #===========================================================================

    #===================================janela saque===================================
    def saque(self):

    	#================================janela========================================
        Window =Tk()
        Window.title('/-/ Banco /-/') #======================titulo======================

        #=============================== widgets ========================================
        descricao=Label(Window,text="Conta:")
        entradaNConta=Entry(Window,width=10)
        descricao2=Label(Window,text="Valor:")
        entradaValor=Entry(Window,width=10)
        feedbackLabel=Label(Window,text="")
        okButton=Button(Window,text="Ok",width=20, command=lambda:controlador.saque(entradaNConta.get(),entradaValor.get(),feedbackLabel))
        #===============================================================================
        #=============================== posicao ========================================
        descricao.place(x=60,y=10)
        entradaNConta.place(x=60,y=30)
        descricao2.place(x=160,y=10)
        entradaValor.place(x=160,y=30)
        feedbackLabel.place(x=60,y=120)
        okButton.place(x=60,y=60)
        #================================================================================
        #==========================size e loop ===========================================
        Window.geometry("300x200+400+200")
        Window.mainloop()
        #==================================================================================

    #================================janela consulta saldo==================================
    def saldo(self):
    		#================================janela=======================================
            Window =Tk()
            Window.title('/-/ Banco /-/') #================titulo==========================
            #==============================================================================
            #============================= widgets ========================================
            descricao=Label(Window,text="Digite o número da conta:")
            entradaNConta=Entry(Window,width=23)
            feedbackLabel=Label(Window,text="")
            okButton=Button(Window,text="Ok",width=20, command=lambda:controlador.saldo(entradaNConta.get(),feedbackLabel))
            #==============================================================================
            #================================ posicao ======================================
            descricao.place(x=60,y=10)
            entradaNConta.place(x=60,y=40)
            feedbackLabel.place(x=60,y=160)
            okButton.place(x=60,y=70)
            #================================================================================
            #===============================seize e loop=====================================
            Window.geometry("300x200+400+200")
            Window.mainloop()
            #================================================================================

    # ======================================== janela deposito =====================================
    def deposito(self):
    	#=======================================janela =============================================
        Window =Tk()
        Window.title('/-/ Banco /-/')
        #===================================== widgets ===========================================
        descricao=Label(Window,text="Conta:")
        entradaNConta=Entry(Window,width=10)
        descricao2=Label(Window,text="Valor:")
        entradaValor=Entry(Window,width=10)
        feedbackLabel=Label(Window,text="")
        okButton=Button(Window,text="Ok",width=20, command=lambda:controlador.deposito(entradaNConta.get(),entradaValor.get(),feedbackLabel))
        #==========================================================================================
        #======================================== posicao ===========================================
        descricao.place(x=60,y=10)
        entradaNConta.place(x=60,y=30)
        descricao2.place(x=160,y=10)
        entradaValor.place(x=160,y=30)
        feedbackLabel.place(x=60,y=120)
        okButton.place(x=60,y=60)
        #===========================================================================================
        #===================================== loop e size=========================================
        Window.geometry("300x200+400+200")
        Window.mainloop()
        #==============================================================================================

    #================================= janela extrato ==================================================
    def extrato(self):
    		#===========================janela =====================================================
            Window =Tk()
            Window.title('/-/ Banco /-/')
            #=======================================================================================
            #================================ widgets ==============================================
            descricao=Label(Window,text="Conta:")
            entradaNConta=Entry(Window,width=10)
            feedbackLabel=Label(Window,text="")
            okButton=Button(Window,text="Gerar",width=10, command=lambda:controlador.extrato(entradaNConta.get(),feedbackLabel))
            #=========================================================================================
            #==================================posicao================================================
            descricao.place(x=60,y=10)
            entradaNConta.place(x=60,y=30)
            feedbackLabel.place(x=60,y=80)
            okButton.place(x=160,y=30)
            #========================================================================================
            #===================================== size e loop =========================================
            Window.geometry("300x350+400+200")
            Window.mainloop()
            #============================================================================================

Set_Gui()