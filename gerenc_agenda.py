from logging import basicConfig
import os
from time import sleep
from datetime import datetime, timedelta
import os.path
from pathlib import Path
from config import Basic_configs

##### VARIÁVEL DO TAMANHO DO LOG
sizeLog     = None
##### VARIÁVEL DO TAMANHO DO LOG ATUALIZADA
newSizeLog  = None
##### NOME DO ARQUIVO EXECUTÁVEL DO ROBÔ
robo_exe = 'ex_agenda.exe'
##### DE QUANTO EM QUANTO TEMPO O ROBÔ EXECUTARÁ A VERIFICAÇÃO
sleep_minutos = Basic_configs.time_verify_gerenciador


print (str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+' - ')+f'Iniciando "{robo_exe}" pela primeira vez...')
os.system('start '+str(robo_exe))

##### A PARTIR DESTE PONTO É UM LOOPING ETERNO
while True:

    ##### NOME DO ARQUIVO DE LOG DO ROBÔ
    robo_log = 'Log_' + Basic_configs.nome_robo + str(datetime.now().strftime('%Y%m%d')) + '.txt'

    print (str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+' - ')+'Verificando '+str(robo_exe))

    ##### CAPTURA O TAMANHO ATUAL DO LOG DO ROBÔ
    try:
        newSizeLog = Path(robo_log).stat().st_size
    except:
        print (str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+' - ')+'excessão - falha na busca o tamanho do log')
        pass


    ##############################################################
    ##### COMPARA O TAMANHO DO LOG ATUAL COM O DA ULTIMA VEZ QUE FEZ A VERIFICAÇÃO
    ##### CASO NÃO TENHA ALTERAÇÃO ELE JÁ REINICIA O ROBÔ
    ##### CASO O LOG ESTEJA SENDO GRAVADO NORMALMENTE, ELE VERIFICA POSTERIORMENTE.
    if sizeLog == newSizeLog:
        print (str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+' - ')+"Será necessário reiniciar "+str(robo_exe))
        os.system('taskkill /F /IM '+str(robo_exe))
        os.system('start '+str(robo_exe))
    else:
        print (str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+' - ')+"Não será feita nenhuma ação no momento...")
    try:
        sizeLog = Path(str(robo_log)).stat().st_size
    except:
        print (str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+' - ')+'excessão - falha ao atualizar a variável do tamanho do log')
        pass
    ##############################################################
            

    print(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+' - ')+f'''Dormirei {sleep_minutos} minutos...''')
    print('\n---------------------------------------------\n')
    # sleep (60)
    sleep (60*sleep_minutos)