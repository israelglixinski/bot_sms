import os
import banco
import threading
from glob import glob
from time import sleep
from queue import Queue
from config import Basic_configs
from conector import Api_infobip
from guipart import Monitor, Color
from datetime import datetime, timedelta

class Application():

    def __init__(self,master,descricao,alvo):
        if alvo == 'agenda':
            alvo = self.agenda
        if alvo == 'contigencia':
            alvo = self.contigencia
        
        self.master= master
        self.queue = Queue()
        self.descricao = descricao
        self.monitor = Monitor(master, self.queue,self.endApplication,self.descricao)
        self.running = 1
        self.periodicCall()
        self.th_acess= threading.Thread(target = alvo).start()

    def periodicCall(self):
        self.monitor.processIncoming()
        self.master.after(200,self.periodicCall)

    def sendMessage(self, message, color=Color.BLACK):
        self.queue.put([message,color])

    def endApplication(self):
        self.running = 0        
        self.master.destroy()
        
    def registrando(self,txt):
        ##### * FORMATO EM QUE FICARÁ A MENSAGEM
        registro = str(datetime.now().strftime('%Y/%m/%d-%H:%M:%S-'))+str(txt)
        ##### * ENVIO DA MENSAGEM PARA O FRONT
        self.sendMessage(registro)
        
        nome_arquivo_log ='Log_' + Basic_configs.nome_robo + str(datetime.now().strftime('%Y%m%d')) + '.txt'
        arquivo_log = open(nome_arquivo_log,'a')
        print (registro, file=arquivo_log)
        arquivo_log.close()

    def apagar_logs(self):
        list_arquivos_log = glob('Log_' + Basic_configs.nome_robo + '*')
        for for_arquivo_log in list_arquivos_log:
            data_arquivo = for_arquivo_log.split(Basic_configs.nome_robo)[1]
            data_arquivo = datetime.strptime(data_arquivo,'%Y%m%d.txt')
            if data_arquivo < datetime.now() - timedelta(days=5):
                os.remove(for_arquivo_log)
            else:
                pass       

    def enviar_sms(self):
        
        self.registrando('Obtendo lista de Numeros para enviar SMS')
        dth_inicio = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        lista_envio = banco.Sms.get_list_sms()
        qtd_sms = len(lista_envio)
        self.registrando ('Foram encontradas '+str(qtd_sms)+' SMS para serem enviadas')
        atual_sms = 0
        for for_envio in lista_envio:
            
            atual_sms = atual_sms+1
            # if atual_sms == 10:
            #     break
            self.registrando ('Trabalhando na SMS '+str(atual_sms)+' de '+str(qtd_sms)+'')
            
            bd_id_cliente_sms_pk        = for_envio[0]
            # bd_nome                     = for_envio[1]
            # bd_dth_atendimento          = for_envio[2]
            bd_enviado                  = for_envio[3]
            # bd_dth_envio                = for_envio[4]
            # bd_respondido               = for_envio[5]
            # bd_dth_retorno              = for_envio[6]
            # bd_nota                     = for_envio[7]
            # bd_obs                      = for_envio[8]
            # bd_id_log_fk                = for_envio[9]
            # bd_id_api_fk                = for_envio[10]
            bd_reenvio                  = for_envio[11]
            bd_id_origem_tipo_fk        = for_envio[12]
            bd_id_origem_cod_fk         = for_envio[13]
            bd_tel                      = for_envio[14]
            bd_sms                      = for_envio[15]
            # bd_canal_atendimento        = for_envio[16]
            bd_msg                      = for_envio[17]
            
                
            enviando_sms = Api_infobip.send_sms('29111', str(bd_tel), str(bd_msg))
            lista_resultados_sms_enviados = enviando_sms.messages
            for for_resultado_sms_enviado in lista_resultados_sms_enviados:
                api_message_id              = for_resultado_sms_enviado.message_id
                # api_to                      = for_resultado_sms_enviado.to
                # api_status_description      = for_resultado_sms_enviado.status.description
                # api_status_group_id         = for_resultado_sms_enviado.status.group_id
                # api_status_group_name       = for_resultado_sms_enviado.status.group_name
                # api_status_id               = for_resultado_sms_enviado.status.id
                # api_status_name             = for_resultado_sms_enviado.status.name
                
            banco.Sms.exec_proc_salva_envio(rec_id_cliente_sms_pk    = bd_id_cliente_sms_pk                           ,
                                            rec_sid_pk               = api_message_id                                 ,
                                            rec_tel                  = bd_tel                                         ,
                                            rec_msg                  = bd_msg                                         ,
                                            rec_dtm_now1             = datetime.now().strftime('%Y-%m-%d %H:%M:%S')   ,
                                            rec_enviado              = bd_enviado                                     ,
                                            rec_reenvio              = bd_reenvio                                     ,
                                            rec_id_origem_tipo_fk    = bd_id_origem_tipo_fk                           ,
                                            rec_id_origem_cod_fk     = bd_id_origem_cod_fk                            ,
                                            rec_dtm_now2             = datetime.now().strftime('%Y-%m-%d %H:%M:%S')   ,
                                            rec_sms                  = bd_sms                                         
                                            )
        
        banco.Sms.exec_proc_alimenta_extrato(
        dth_inicio   = str(dth_inicio),
        dth_final    = datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
        enviados     = qtd_sms,
        falha        = 0,
        total        = qtd_sms,
        tipo         = 'Envio'
        )
        
        self.registrando('Conluido envio de SMS')

    def receber_sms(self):
        self.registrando ('Verificando recebimento de SMS')
        dth_inicio = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        novas_sms               = Api_infobip.receive_sms()
        messageCount            =novas_sms.messageCount        
        pendingMessageCount     =novas_sms.pendingMessageCount
        self.registrando('Recebido '+str(messageCount)+' SMS da API')
        self.registrando('Ficarão '+str(pendingMessageCount)+' pendentes')
        self.registrando('Salvando SMS no banco de dados')
        for for_sms in novas_sms.results:
            try:
                sms_messageId               = for_sms.messageId             
                sms_to                      = for_sms.to                    
                sms_text                    = for_sms.text                  
                # sms_cleanText               = for_sms.cleanText             
                # sms_receivedAt              = for_sms.receivedAt            
                # sms_smsCount                = for_sms.smsCount              
                sms_pairedMessageId         = for_sms.pairedMessageId       
                # sms_price_pricePerMessage   = for_sms.price.pricePerMessage 
                # sms_price_currency          = for_sms.price.currency        
                sms_from                    = for_sms.phrom
                
                banco.Sms.exec_proc_salva_resposta(
                    resp_id_resposta    = str(sms_messageId),
                    resp_id_api_fk      = str(sms_pairedMessageId),  
                    resp_carrier_id     ='NULL',  
                    resp_carrier_name   ='NULL',  
                    resp_source         = str(sms_from),
                    resp_short_code     = str(sms_to),
                    resp_message_text   = str(sms_text),
                    resp_receive_at     ='NULL',  
                    resp_receive_date   =datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  
                    resp_mt_user_name   ='c071013-geacr',  
                    resp_mt_email       ='jose.guanaes@caixa.gov.br',  
                    resp_correlationId  ='Vazio'              
                )
                self.registrando(f'Salvo resposta {str(sms_messageId)} com sucesso ')
            except:
                self.registrando('Erro ao tentar salvar uma resposta SMS')
        banco.Sms.exec_proc_alimenta_extrato(
        dth_inicio   = str(dth_inicio),
        dth_final    = datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
        enviados     = messageCount,
        falha        = 0,
        total        = messageCount,
        tipo         = 'Tratamento'
        )        
            
        self.registrando('Concluído armazenamento de SMS recebidas') 
        
    def relatorio_extrato(self):

        self.registrando('Iniciando relatorio_extrato de SMS')

        dth_inicio = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        list_extrato = banco.Sms.get_relatorio_extrato()
        total_extrato = 0
        sleep (3)
        for item_extrato in list_extrato:
            total_extrato = total_extrato + item_extrato[0]

        banco.Sms.exec_proc_alimenta_extrato(
        dth_inicio   = str(dth_inicio),
        dth_final    = datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
        enviados     = total_extrato,
        falha        = 0,
        total        = total_extrato,
        tipo         = 'Lista de status'
        ) 
        
        self.registrando('Finalizado relatorio_extrato de SMS')
        
    def agenda(self):
        
        self.registrando('Inicializado o Robô SMS - Versão '+Basic_configs.versao)
        
        list_hora_exec = [
        '08:00',
        '09:00',
        '10:00',
        '11:00',
        '12:00',
        '13:00',
        '14:00',
        '15:00',
        '16:00',
        '17:00',
        '18:00'
        ]
        
        while self.running:
            ##### VERIFICA SE ESTÁ NO HORARIO DE ENVIO E RECEBIMENTO DE SMS
            for for_hora_exec in list_hora_exec:
                if str(datetime.now().strftime('%H:%M')) == for_hora_exec:
                    self.registrando('Iniciando o agendamento das '+str(for_hora_exec))
                    self.registrando('Versão Atual do Robô: '+Basic_configs.versao) 
                    self.receber_sms()
                    self.enviar_sms()
                    self.apagar_logs()
                    self.registrando('Finalizado execução da rotina')
                    sleep(60)
            
            self.registrando('...')
            sleep(30)
        
    def contigencia(self):
        self.registrando('Iniciando execução de contigência')
        self.registrando('Versão Atual do Robô: '+Basic_configs.versao) 
        # self.receber_sms()
        # self.enviar_sms()
        self.apagar_logs()
        self.registrando('Finalizado execução da rotina')                
        self.registrando('Esta janela já pode ser fechada')        
