import os
import mimetypes
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class EmailModel:
    def __init__(self, sender_address: str, recipient_address: str, subject: str, body: str, attachments: list = None):
        """
        Class model for an email message.

        Args:
            sender_address (str): Email address of the sender.
            recipient_address (str): Email address of the recipient.
            subject (str): Subject of the email.
            body (str): Body content of the email (HTML format).
            attachments (list): List of file paths to attach to the email.
        """
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.subject = subject
        self.body = body
        self.attachments = attachments or []

    def create_message(self) -> EmailMessage:
        """
        Create an email message from the model's attributes.
        """
        # If there are attachments, use MIMEMultipart
        if self.attachments:
            msg = MIMEMultipart()
            msg['Subject'] = self.subject
            msg['From'] = self.sender_address
            msg['To'] = self.recipient_address
            
            corpo = MIMEText(self.body, 'html')
            print(corpo)
            # Adicionar corpo do email
            msg.attach(corpo)
            
            # Adicionar anexos
            for attachment_path in self.attachments:
                if os.path.isfile(attachment_path):
                    self._add_attachment(msg, attachment_path)
        else:
            # Sem anexos, usar EmailMessage simples
            msg = EmailMessage()
            msg['Subject'] = self.subject
            msg['From'] = self.sender_address
            msg['To'] = self.recipient_address
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