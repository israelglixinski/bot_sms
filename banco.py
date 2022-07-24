
##### * ARQUIVO RESPONSÁVEL PELA CONEXÃO E AÇÕES COM O BANCO DE DADOS

##### * IMPORTAÇÃO DAS BIBLIOTECAS
import pyodbc
import os
from config import Basic_configs
from datetime import datetime, timedelta


##### * CONEXÃO COM BANCO RESPONSÁVEL PELO GERENCIAMENTO DE ROBÔS
conn_robo = pyodbc.connect("DRIVER={SQL Server};"
            "SERVER="   + str(Basic_configs.Bd.Sms.HOST) + ";"
            "DATABASE=" + str(Basic_configs.Bd.Sms.NAME) + ";"
            "UID="      + str(Basic_configs.Bd.Sms.USER) + ";"
            "PWD="      + str(Basic_configs.Bd.Sms.PASS),
            autocommit = True )
    
##### * CONEXÃO COM O BANCO RESPONSÁVEL PELAS SMS    
conn_sms = pyodbc.connect("DRIVER={SQL Server};"
            "SERVER="   + str(Basic_configs.Bd.Sms.HOST) + ";"
            "DATABASE=" + str(Basic_configs.Bd.Sms.NAME) + ";"
            "UID="      + str(Basic_configs.Bd.Sms.USER) + ";"
            "PWD="      + str(Basic_configs.Bd.Sms.PASS),
            autocommit = True )    
    

class Robo():
    '''Classe para trabalhar com o controle de fluxo dos robôs, 
    no momento esta classe não está sendo utilizada, 
    ainda em desenvolvimento'''
    
    def check_logged():
        '''Funcão que verifica a ultima execução do robô'''
        retorno = False
        try:
            cur = conn_robo.cursor()
            cur.execute("SELECT DH_STATUS FROM [BANCO].[SCHEMA].[TABELA] WHERE [COLUNA]='NOME_ROBO'")
            res = cur.fetchone()
            if res!=None:
                # ##### TRATAMENTO DAS INFORMAÇÕES OBTIDAS NO BANCO DE DADOS
                res = str(res).replace(' ','')
                res = str(res).replace('(','')
                res = str(res).replace(')','')
                res = str(res).replace('datetime.datetime','')
                retorno = res
            else:
                retorno = '2021,5,12,9,14,22,610000,'
                
        except pyodbc.Error as e:
            lastError = format(e)
            retorno = lastError
            pass
        return retorno
    
    
class Sms():
    '''Classe responsável pelas ações no banco de dados das SMS'''
    
    def get_list_sms():
        cur = conn_sms.cursor()
        sql = f'''SELECT DH_STATUS FROM [BANCO].[SCHEMA].[TABELA]'''
        cur.execute(sql)   
        res = cur.fetchall()
        return res
   
    def salva_envio():
        
        cur = conn_sms.cursor()
        
        sql = f'''
            '''
        cur.execute(sql)   
        
    def salva_resposta():
        
        cur = conn_sms.cursor()
        
        sql = f'''
            '''        

        cur.execute(sql)

