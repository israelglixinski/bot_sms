import tkinter
from tkinter import ttk
from enum import Enum

class Painel:
    botao1 = None
    contProgress = 0
    lineCounter = 1 #contador para as linhas de mensagens que serao exibidas na tela
    
    def __init__(self,master,queue,botao1,endCommand):
        self.queue = queue
        self.master = master
        self.botao1 = botao1
        self.create_widgets()
        self.master.protocol("WM_DELETE_WINDOW",endCommand)

    def create_widgets(self):
        """Metodo que monta os objetos de tela
        """
        #cria um frame no topo com 50 px de altura para armazenar os items do login
        frameLogin = tkinter.Frame(self.master,padx=0,pady=5)
        frameLogin.pack(fill=tkinter.X)

        #cria um frame no topo com 50 px de altura para armazenar os botões
        frameBtn = tkinter.Frame(self.master,padx=0,pady=5)
        frameBtn.pack(fill=tkinter.X)

        #cria um frame para armazenar a progressbar
        frameBar = tkinter.Frame(self.master)
        frameBar.pack(fill=tkinter.X)

        #cria um botao primario
        self.btnExecute = tkinter.Button(frameBtn,text="Iniciar",command=self.botao1)
        self.btnExecute.pack(side=tkinter.LEFT)

        #cria um progressbar para deixar bonita a exibicao  (precisa ser self pois eh usado em outro metodo)
        self.progress = ttk.Progressbar(frameBar,orient='horizontal',mode='determinate',length=630)
        self.progress.pack(fill=tkinter.BOTH)

class Monitor:
    loginCommand = None
    contProgress = 0
    lineCounter = 1 #contador para as linhas de mensagens que serao exibidas na tela
    
    def __init__(self,master,queue,endCommand,descricao):
        self.queue = queue
        self.master = master
        self.descricao = descricao
        self.create_widgets()
        self.master.protocol("WM_DELETE_WINDOW",endCommand)

    def create_widgets(self):
        """Metodo que monta os objetos de tela
        """
        #cria um frame no topo com 50 px de altura para armazenar informações
        frameLabel = tkinter.Frame(self.master,padx=0,pady=5)
        frameLabel.pack(fill=tkinter.X)

        #cria um label login e um text para login
        lblLogin = tkinter.Label(frameLabel,text=self.descricao)
        lblLogin.pack(side=tkinter.LEFT)

        #cria um frame npara armazenar os items de texto
        frameTexto = tkinter.Frame(self.master)
        frameTexto.pack(fill=tkinter.X)

        #cria um frame para armazenar a progressbar
        # frameBar = tkinter.Frame(self.master)
        # frameBar.pack(fill=tkinter.X)

        #cria um text para resultado dos logs (precisa ser self pois eh usado em outro metodo)
        self.txtResult = tkinter.Text(frameTexto)
        self.txtResult.pack(side=tkinter.LEFT)
        
        #cria um scrollbar para a rolagem do text
        scrl = tkinter.Scrollbar(frameTexto,command=self.txtResult.yview)
        scrl.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.txtResult["yscrollcommand"] = scrl.set

        # #cria um progressbar para deixar bonita a exibicao  (precisa ser self pois eh usado em outro metodo)
        # self.progress = ttk.Progressbar(frameBar,orient='horizontal',mode='determinate',length=630)
        # self.progress.pack(fill=tkinter.BOTH)

        #cores das linhas para exibir nas mensagens de tela
        self.txtResult.tag_config(Color.RED.name,   foreground=Color.RED.value)
        self.txtResult.tag_config(Color.GREEN.name, foreground=Color.GREEN.value)
        self.txtResult.tag_config(Color.ORANGE.name,foreground=Color.ORANGE.value)
        self.txtResult.tag_config(Color.PURPLE.name,foreground=Color.PURPLE.value)
        self.txtResult.tag_config(Color.INDIGO.name,foreground=Color.INDIGO.value) 
        self.txtResult.tag_config(Color.BROWN.name, foreground=Color.BROWN.value)
        self.txtResult.tag_config(Color.TOMATO.name,foreground=Color.TOMATO.value)
        self.txtResult.tag_config(Color.BLUE.name,  foreground=Color.BLUE.value)

    # def unlock_clear(self):
    #     """Realiza a limpeza dos campos e desbloqueio do botao executar
    #     """        
    #     self.btnExecute["state"] = "normal"
    #     self.txtResult.delete('1.0',tkinter.END)
    #     return None

    # def runProgress(self,value):
    #     """Metodo que executa a progressBar

    #     Args:
    #         value (int): Total de Registros, ou seja, o 100% da barra
    #     """
    #     #realiza o incremento no progressbar
    #     if self.progress['value'] < 100:
    #         #atualiza a barra de progresso
    #         try:
    #             self.progress['value'] = (self.contProgress*100)/value
    #         except ZeroDivisionError:
    #             pass
    #         #incrementa o contador de progresso
    #         self.contProgress +=1

    # def startProgressIndeterminate(self):
    #     """Executa a barra de progresso em modo intermitente, ou seja, apenas vai-e-vem
    #     """
    #     self.progress["mode"] = "indeterminate"
    #     self.progress.start()

    # def stopProgressIndeterminate(self):
    #     """Metodo para a barra de progresso e volta para o modo determinado
    #     """
    #     self.progress["value"] = 0
    #     self.contProgress = 0 
    #     self.progress["mode"] = "determinate"
    #     self.progress.stop()

    # def setStartSince(self,data):
    #     """Metodo que determina a data de execucao inicial do sistema

    #     Args:
    #         data (str): Data jah formatada
    #     """
    #     self.lblSince["text"] = "Executando desde: " + data

    # def resetProgress(self):
    #     """Metodo que realiza um reset na barra de progresso
    #     """
    #     self.progress['value'] = 0
    #     self.contProgress = 0

    # def clearLogScreen(self):
    #     """Metodo que limpa a tela de logs
    #     """
    #     self.lineCounter = 1
    #     self.txtResult.delete('1.0',tkinter.END)

    def processIncoming(self):
        """Metodo que envia a mensagem para a tela ou para o log
        """
        while self.queue.qsize():
            que = self.queue.get()
            msg = que[0]
            cor = que[1]
            self.lineCounter += 1
            if cor!=None:
                self.txtResult.insert(str(self.lineCounter)+'.0',str(msg)+'\n',cor.name)
            else:
                self.txtResult.insert(str(self.lineCounter)+'.0',str(msg)+'\n')
            self.txtResult.see("end")


class Color(Enum):
    RED    = '#FF0000' #RED
    GREEN  = '#006400' #DARKGREEN
    ORANGE = '#FF8C00' #DARKORANGE
    PURPLE = '#A020F0' #PURPLE
    INDIGO = '#4B0082' #INDIGO
    BROWN  = '#8B4513' #SADDLEBROWN
    TOMATO = '#FF6347' #TOMATO
    BLUE   = '#4169e1' #ROYALBLUE
    BLACK  = '#000000' #BLACK

