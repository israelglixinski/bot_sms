
########################################################################################
##### * ARQUIVO COM AS CONFIGURAÇÕES DO ROBÔ.
########################################################################################

from datetime import datetime
class Basic_configs():
    '''Classe com as configurações básicas do Robô'''    
    
    versao                  ='1.0.0'
    nome_robo               ='bot_sms'
    nome_arquivo_exec       =nome_robo + versao + '.exe'
    nome_arquivo_log        ='Log_' + nome_robo + str(datetime.now().strftime('%Y%m%d')) + '.txt'
    time_verify_gerenciador = 25
    
    class Api():       
        '''AMBIENTES DE ENVIO DE SMS PELO API - INFOBIP'''

        class Israel():
            BASE_URL  = "https://gy2wqj.api.infobip.com"
            API_KEY   = "f67742dea59d7244357ba167d0a5c0e2-415ec7dc-874d-46ca-98ee-3d0dc3ba14ac"
        
    class Bd():
        '''CONEXÕES COM BANCO DE DADOS'''
        
        class Robo():
            HOST = ''
            NAME = ''
            USER = ''
            PASS = ''

        class Sms():
            HOST = ''
            NAME = ''
            USER = ''
            PASS = ''
    

    
    
    
    
    
    
    
    

    