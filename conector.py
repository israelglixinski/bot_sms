
##### *ARQUIVO COM AS CONEXÕES EXTERNAS, EXEMPLO: API, SITE, ETC... 
##### *NO CASO ESPECÍFICO DESTE ROBÔ SERÁ TRABALHANDO SOMENTE COM A API DA INFOBIP

##### *IMPORTAÇÃO DAS BIBLIOTECAS RESPONSÁVEIS PELA CONEXÃO COM A API DA IMFOBIP 
from infobip_api_client.api_client import ApiClient, Configuration
from infobip_api_client.model.sms_advanced_textual_request import SmsAdvancedTextualRequest
from infobip_api_client.model.sms_destination import SmsDestination
from infobip_api_client.model.sms_response import SmsResponse
from infobip_api_client.model.sms_textual_message import SmsTextualMessage
from infobip_api_client.api.send_sms_api import SendSmsApi
from infobip_api_client.exceptions import ApiException

##### *IMPORTAÇÃO DAS DEMAIS BIBLIOTECAS
from config import Basic_configs
import requests
import json
from types import SimpleNamespace

##### *DECLARAÇÃO DAS VARIÁVEIS GLOBAIS
nav = requests.Session()
base_url    = Basic_configs.Api.Caixa.BASE_URL
api_key     = Basic_configs.Api.Caixa.API_KEY
# nav.proxies = {'http': '', 'https': ''}
nav.headers = {'Authorization':'App '+api_key}

class Api_infobip():
    '''Classe responsável pela conexão ao API da INFOBIP'''
    
    def send_sms(remetente, telefone, texto_mensagem):
        """
        #  Envia SMS através do API da Infobip
        
        # Parâmetros:
            * remetente: Quem está enviando a SMS
            * telefone: Destinatário
            * texto_mensagem: Conteudo da SMS
       
        # Retorno:
            * Sucesso:    Dados da SMS enviada
            * Falha:      Erro ocorrido  
        """
                
        # * Send an sms message by using Infobip API.
        # *
        # * This example is already pre-populated with your account data:
        # * 1. Your account Base URL
        # * 2. Your account API key
        # * 3. Your recipient phone number
        # *
        # * THIS CODE EXAMPLE IS READY BY DEFAULT. HIT RUN TO SEND THE MESSAGE!
        # *
        # * Send sms API reference: https://www.infobip.com/docs/api#channels/sms/send-sms-message
        # * See Readme file for details.

        ##### PARAMETROS DE ENVIO DA SMS
        SENDER          = remetente
        RECIPIENT       = telefone
        MESSAGE_TEXT    = texto_mensagem

        client_config = Configuration(
                host= base_url,
                api_key={"APIKeyHeader": api_key},
                api_key_prefix={"APIKeyHeader": "App"},
            )

        api_client = ApiClient(client_config)

        sms_request = SmsAdvancedTextualRequest(
                messages=[
                    SmsTextualMessage(
                        destinations=[
                            SmsDestination(
                                to=RECIPIENT,
                            ),
                        ],
                        _from=SENDER,
                        text=MESSAGE_TEXT,
                    )
                ])

        api_instance = SendSmsApi(api_client)

        try:
            api_response: SmsResponse = api_instance.send_sms_message(sms_advanced_textual_request=sms_request)
            retorno = api_response
        except ApiException as ex:
            print("Ocorreu um Erro ao tentar enviar a menssagem de SMS")
            retorno = ex
        return retorno
    
    def receive_sms():
        '''
        # Responsável pelo recebimento das SMS enviadas pelos clientes.
            * Não recebe parâmetros
        # Retorno:
            * Sucesso: Objeto Json
            * Falha: None
        '''
        #####*Faz a requisição à API 
        novas_sms = nav.get(base_url+'/sms/1/inbox/reports?limit=1000')
        #####*Em caso de resposta positiva
        if(novas_sms.status_code==200):
            #####*Já faz o retorno da resposta convertido em json
            return json.loads((novas_sms.text).replace("from","phrom"),object_hook=lambda d: SimpleNamespace(**d))
        return None 
    
    
    