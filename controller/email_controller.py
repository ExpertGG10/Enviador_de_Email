# email_controller.py
import os
import smtplib
import mimetypes
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
        - body (str): Corpo do email (HTML).
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
        - body (str): Corpo do email (HTML).
        - attachments (list): Lista de caminhos para arquivos anexos.
        """
        logger.debug(f"[EMAIL] Criando EmailModel para: {recipientAddress}")
        if attachments:
            logger.debug(f"[ANEXO] {len(attachments)} anexo(s) a serem enviados")
        
        try:
            emailModel = EmailModel(self.senderAddress, recipientAddress, subject, body, attachments)
            msg = emailModel.createMessage()

            # Force o corpo para HTML SEM alterar o EmailModel
            try:
                # 1) Coletar anexos já existentes (se o model os tiver criado)
                existing_attachments = []
                if msg.is_multipart():
                    for part in msg.iter_attachments():
                        existing_attachments.append(part)

                # 2) Limpar o conteúdo e setar o HTML como corpo principal
                #    (mantém headers como From, To, Subject, Date, Message-ID)
                msg.clear_content()
                msg.set_content(body, subtype="html", charset="utf-8")

                # 3) Reanexar anexos que já estavam na mensagem
                for part in existing_attachments:
                    data = part.get_payload(decode=True)
                    ctype = part.get_content_type()
                    maintype, subtype = ctype.split("/", 1)
                    filename = part.get_filename()
                    msg.add_attachment(data, maintype=maintype, subtype=subtype, filename=filename)

                # 4) Se o modelo não anexou nada, mas o controller recebeu attachments,
                #    anexe aqui (fallback para garantir envio)
                if not existing_attachments and attachments:
                    for path in attachments:
                        if not path:
                            continue
                        ctype, encoding = mimetypes.guess_type(path)
                        if ctype is None or encoding is not None:
                            ctype = "application/octet-stream"
                        maintype, subtype = ctype.split("/", 1)
                        with open(path, "rb") as f:
                            data = f.read()
                        msg.add_attachment(
                            data,
                            maintype=maintype,
                            subtype=subtype,
                            filename=os.path.basename(path),
                        )

                logger.debug("[EMAIL] Corpo forçado para HTML e anexos consolidados")
            except Exception as adjust_err:
                # Caso algo falhe na conversão para HTML, registra e tenta enviar do jeito que veio
                logger.warning(f"[WARN] Nao foi possivel ajustar o corpo para HTML via controller: {adjust_err}. Enviando como criado pelo modelo.")

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
        try:
            self.smtpServer.quit()
        except Exception:
            # Evita exceção durante garbage collection se a conexão já estiver fechada
            pass
        logger.debug("[OK] Conexao SMTP fechada")