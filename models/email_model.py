import os
import mimetypes
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class EmailModel:
    def __init__(self, senderAddress: str, recipientAddress: str, subject: str, body: str, attachments: list = None):
        """
        Classe para representar um modelo de email.

        params:
        - senderAddress (str): Endereço de email do remetente.
        - recipientAddress (str): Endereço de email do destinatário.
        - subject (str): Assunto do email.
        - body (str): Corpo do email.
        - attachments (list): Lista de caminhos para arquivos anexos.
        """
        self.senderAddress = senderAddress
        self.recipientAddress = recipientAddress
        self.subject = subject
        self.body = body
        self.attachments = attachments or []

    def createMessage(self) -> EmailMessage:
        """
        Cria uma mensagem de email a partir dos atributos do modelo.
        """
        # Se há anexos, usar MIMEMultipart
        if self.attachments:
            msg = MIMEMultipart()
            msg['Subject'] = self.subject
            msg['From'] = self.senderAddress
            msg['To'] = self.recipientAddress
            
            # Adicionar corpo do email
            msg.attach(MIMEText(self.body, 'plain', 'utf-8'))
            
            # Adicionar anexos
            for attachment_path in self.attachments:
                if os.path.isfile(attachment_path):
                    self._add_attachment(msg, attachment_path)
        else:
            # Sem anexos, usar EmailMessage simples
            msg = EmailMessage()
            msg['Subject'] = self.subject
            msg['From'] = self.senderAddress
            msg['To'] = self.recipientAddress
            msg.set_content(self.body)
        
        return msg
    
    def _add_attachment(self, msg: MIMEMultipart, file_path: str):
        """
        Adiciona um anexo à mensagem.
        
        Args:
            msg: Mensagem MIMEMultipart
            file_path: Caminho para o arquivo anexo
        """
        try:
            # Detectar tipo MIME do arquivo
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type is None:
                mime_type = 'application/octet-stream'
            
            main_type, sub_type = mime_type.split('/', 1)
            
            # Ler arquivo
            with open(file_path, 'rb') as attachment:
                part = MIMEBase(main_type, sub_type)
                part.set_payload(attachment.read())
            
            # Codificar em base64
            encoders.encode_base64(part)
            
            # Adicionar cabeçalhos do anexo
            filename = os.path.basename(file_path)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {filename}'
            )
            
            # Anexar à mensagem
            msg.attach(part)
            
        except Exception as e:
            # Log do erro mas não interrompe o envio
            print(f"Erro ao anexar arquivo {file_path}: {e}")