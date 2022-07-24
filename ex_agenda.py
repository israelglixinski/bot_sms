from config import Basic_configs
import tkinter 
from pkg_resources import resource_filename
from aplicacao import Application

descricao = 'Executa a rotina a cada 1 hora'
janela = 'agenda'

#cria o objeto principal do sistema (tela mae)
root = tkinter.Tk()
icone = resource_filename(__name__, 'fire.ico')
#adiciona o icone da tela
root.iconbitmap(icone)
#dah um titulo para a tela
root.title(Basic_configs.nome_robo+''+Basic_configs.versao+' '+janela)
#bloqueia a possibilidade do usuario mexer no tamanho da tela
root.resizable(False,False)
#define um tamanho padrao para a tela
root.geometry("670x440")
#inicia a aplicacao passando a tela e a thread mae do processo
app = Application(root, descricao, janela)
#inicia a thread de execucao da tela
root.mainloop()



