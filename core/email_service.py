import logging
from typing import List, Dict, Any
from dao.email_dao import EmailDao
from controller.email_controller import EmailController
from utils.exceptions import EmailServiceError

logger = logging.getLogger(__name__)


class EmailService:
    """
    Serviço central para gerenciar operações de email.
    Coordena entre DAO, Controller e validações.
    """
    
    def __init__(self):
        self.dao = None
        self.controller = None
    
    def configure_sender(self, sender_email: str, app_password: str) -> bool:
        """
        Configura o remetente e autenticação.
        
        Args:
            sender_email: Email do remetente
            app_password: Senha de aplicativo
            
        Returns:
            bool: True se configuração foi bem-sucedida
            
        Raises:
            EmailServiceError: Se configuração falhar
        """
        logger.info(f"[CONFIG] Configurando remetente: {sender_email}")
        try:
            self.controller = EmailController(app_password, sender_email)
            logger.info("[OK] Remetente configurado com sucesso")
            return True
        except Exception as e:
            logger.error(f"[ERRO] Erro ao configurar remetente: {e}")
            raise EmailServiceError(f"Erro ao configurar remetente: {e}")
    
    def process_recipient_file(self, file_path: str) -> List[str]:
        """
        Processa arquivo de destinatários e extrai emails válidos.
        
        Args:
            file_path: Caminho para arquivo Excel/CSV
            
        Returns:
            List[str]: Lista de emails válidos
            
        Raises:
            EmailServiceError: Se processamento falhar
        """
        logger.info(f"[FILE] Processando arquivo: {file_path}")
        try:
            self.dao = EmailDao(file_path)
            logger.debug("[OK] EmailDAO criado")
            
            emails = self.dao.getEmails()
            logger.info(f"[EMAIL] {len(emails)} emails extraidos do arquivo")
            
            if not emails:
                logger.warning("[WARN] Nenhum email valido encontrado no arquivo")
                raise EmailServiceError("Nenhum email válido encontrado no arquivo")
            
            logger.debug(f"[EMAIL] Emails encontrados: {emails[:5]}{'...' if len(emails) > 5 else ''}")
            return emails
        except Exception as e:
            logger.error(f"[ERRO] Erro ao processar arquivo: {e}")
            raise EmailServiceError(f"Erro ao processar arquivo: {e}")
    
    def send_bulk_emails(self, recipients: List[str], subject: str, body: str, attachments: List[str] = None) -> Dict[str, Any]:
        """
        Envia emails em massa.
        
        Args:
            recipients: Lista de destinatários
            subject: Assunto do email
            body: Corpo do email
            attachments: Lista de caminhos para arquivos anexos
            
        Returns:
            Dict com resultado da operação
            
        Raises:
            EmailServiceError: Se envio falhar
        """
        logger.info(f"[EMAIL] Iniciando envio em massa para {len(recipients)} destinatarios")
        logger.debug(f"[EMAIL] Assunto: {subject}")
        logger.debug(f"[EMAIL] Corpo: {body[:100]}{'...' if len(body) > 100 else ''}")
        if attachments:
            logger.info(f"[ANEXO] {len(attachments)} anexo(s) serão enviados")
        
        if not self.controller:
            logger.error("[ERRO] Remetente nao configurado")
            raise EmailServiceError("Remetente não configurado")
        
        try:
            logger.debug("[PROCESS] Chamando controller.sendMassEmails...")
            success = self.controller.sendMassEmails(recipients, subject, body, attachments)
            logger.info(f"[OK] Envio concluido: {'sucesso' if success else 'falha'}")
            
            return {
                'success': success,
                'recipients_count': len(recipients),
                'attachments_count': len(attachments) if attachments else 0,
                'message': 'Emails enviados com sucesso' if success else 'Falha no envio'
            }
        except Exception as e:
            logger.error(f"[ERRO] Erro ao enviar emails: {e}")
            raise EmailServiceError(f"Erro ao enviar emails: {e}")
    
    def validate_email_data(self, sender: str, recipients: List[str], subject: str, body: str) -> bool:
        """
        Valida dados de email antes do envio.
        
        Args:
            sender: Email do remetente
            recipients: Lista de destinatários
            subject: Assunto
            body: Corpo
            
        Returns:
            bool: True se dados são válidos
            
        Raises:
            EmailServiceError: Se validação falhar
        """
        if not sender or '@' not in sender:
            raise EmailServiceError("Email do remetente inválido")
        
        if not recipients:
            raise EmailServiceError("Lista de destinatários vazia")
        
        if not subject.strip():
            raise EmailServiceError("Assunto não pode estar vazio")
        
        if not body.strip():
            raise EmailServiceError("Corpo do email não pode estar vazio")
        
        return True
