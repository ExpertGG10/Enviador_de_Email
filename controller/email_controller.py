import smtplib
import logging
from models.email_model import EmailModel

logger = logging.getLogger(__name__)

class EmailController:
    def __init__(self, appPassword: str, senderAddress: str):
        """
        Controlador para gerenciar o envio de emails.
        
        params:
        - appPassword (str): Senha de aplicativo para autenticação SMTP.
        - senderAddress (str): Endereço de email do remetente.
        """
        logger.info(f"[INIT] Inicializando EmailController para: {senderAddress}")

        self.appPassword = appPassword
        self.senderAddress = senderAddress

        logger.debug("[SMTP] Conectando ao servidor SMTP...")
        self.smtpServer = smtplib.SMTP_SSL('smtp.gmail.com', 465) 
        logger.debug("[OK] Conexao SMTP estabelecida")

        logger.debug("[AUTH] Fazendo login no servidor...")
        self.smtpServer.login(self.senderAddress, self.appPassword)
        logger.info("[OK] Login SMTP realizado com sucesso")

    def sendMassEmails(self, recipientList: list[str], subject: str, body: str, attachments: list = None):
        """
        Envia emails em massa para uma lista de destinatários.

        params:
        - recipientList (list[str]): Lista de endereços de email dos destinatários.
        - subject (str): Assunto do email.
        - body (str): Corpo do email.
        - attachments (list): Lista de caminhos para arquivos anexos.
        """
        logger.info(f"[EMAIL] Iniciando envio em massa para {len(recipientList)} destinatarios")
        logger.debug(f"[EMAIL] Assunto: {subject}")
        if attachments:
            logger.info(f"[ANEXO] {len(attachments)} anexo(s) serão enviados com cada email")
        
        try:
            for i, recipient in enumerate(recipientList, 1):
                logger.debug(f"[EMAIL] Enviando email {i}/{len(recipientList)} para: {recipient}")
                self.sendEmail(recipient, subject, body, attachments)
                logger.debug(f"[OK] Email {i} enviado com sucesso")
            
            logger.info("[OK] Todos os emails foram enviados com sucesso")
            return True
        except smtplib.SMTPAuthenticationError:
            logger.error("[ERRO] Erro de autenticacao SMTP")
            raise ValueError("Erro de autenticação! Verifique o email e a senha de aplicativo.")
        except Exception as e:
            logger.error(f"[ERRO] Erro no envio em massa: {e}")
            raise Exception(f"Ocorreu um erro: {e}")
        
    def sendEmail(self, recipientAddress: str, subject: str, body: str, attachments: list = None):
        """
        Envia um email para um destinatário específico.
        
        params:
        - recipientAddress (str): Endereço de email do destinatário.
        - subject (str): Assunto do email.
        - body (str): Corpo do email.
        - attachments (list): Lista de caminhos para arquivos anexos.
        """
        logger.debug(f"[EMAIL] Criando EmailModel para: {recipientAddress}")
        if attachments:
            logger.debug(f"[ANEXO] {len(attachments)} anexo(s) a serem enviados")
        
        try:
            emailModel = EmailModel(self.senderAddress, recipientAddress, subject, body, attachments)
            msg = emailModel.createMessage()
            logger.debug(f"[EMAIL] Enviando mensagem para: {recipientAddress}")
            self.smtpServer.send_message(msg)
            logger.debug(f"[OK] Email enviado com sucesso para: {recipientAddress}")
        except smtplib.SMTPAuthenticationError:
            logger.error(f"[ERRO] Erro de autenticacao ao enviar para: {recipientAddress}")
            raise ValueError("Erro de autenticação! Verifique o email e a senha de aplicativo.")
        except Exception as e:
            logger.error(f"[ERRO] Erro ao enviar email para {recipientAddress}: {e}")
            raise Exception(f"Ocorreu um erro: {e}")
        
    def __del__(self):
        logger.debug("[SMTP] Fechando conexao SMTP...")
        self.smtpServer.quit()
        logger.debug("[OK] Conexao SMTP fechada")