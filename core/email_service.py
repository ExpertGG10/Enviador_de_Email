import logging
from typing import List, Dict, Any, Optional

from dao.recipient_dao import RecipientDao
from dao.sender_dao import SenderDao
from dao.recipient_group_dao import RecipientGroupDao
from controller.email_controller import EmailController
from utils.exceptions import EmailServiceError

logger = logging.getLogger(__name__)


class EmailService:
    """
    Serviço central para gerenciar operações de email.
    Coordena entre DAOs, Controller e validações.
    """

    def __init__(self, recipient_path: Optional[str] = None, sender_path: Optional[str] = None, group_path: Optional[str] = None):
        self.recipient_dao = RecipientDao(recipient_path)
        self.sender_dao = SenderDao(sender_path)
        self.group_dao = RecipientGroupDao(group_path)
        self.controller: Optional[EmailController] = None

    # ------------------------
    # Groups CRUD via DAO
    # ------------------------
    def add_group(self, name: str) -> Dict[str, Any]:
        try:
            grp = self.group_dao.add(name)
            logger.info(f"[SERVICE] Group added: {name}")
            return grp
        except Exception as e:
            logger.error(f"[ERRO] Erro ao adicionar grupo: {e}")
            raise EmailServiceError(str(e))

    def list_groups(self) -> List[Dict[str, Any]]:
        return self.group_dao.list_all()


    def delete_group(self, group_id: int) -> bool:
        try:
            deleted = self.group_dao.delete(group_id)
            if deleted:
                # Reset groupId em recipients que pertenciam ao grupo
                for r in self.recipient_dao.list_all():
                    if r.get("groupId") == group_id:
                        try:
                            self.recipient_dao.update(r["id"], groupId=0)
                        except Exception:
                            logger.warning(f"[WARN] Falha ao resetar groupId do recipient {r.get('id')}")
                logger.info(f"[SERVICE] Grupo {group_id} deletado e membros atualizados")
            return deleted
        except Exception as e:
            logger.error(f"[ERRO] Erro ao deletar grupo: {e}")
            raise EmailServiceError(str(e))

    def add_recipient_to_group(self, recipient_id: int, group_id: int) -> bool:
        try:
            # atualiza recipient
            self.recipient_dao.update(recipient_id, groupId=group_id)
            # atualiza grupo (lista de ids)
            self.group_dao.add_recipient_to_group(group_id, recipient_id)
            return True
        except Exception as e:
            logger.error(f"[ERRO] Erro ao adicionar recipient {recipient_id} ao grupo {group_id}: {e}")
            raise EmailServiceError(str(e))


    def list_group_recipients(self, group_id: int) -> List[Dict[str, Any]]:
        grp = self.group_dao.find_by_id(group_id)
        if not grp:
            raise EmailServiceError("Grupo não encontrado")
        members = []
        for rid in grp.get("recipients", []):
            r = next((x for x in self.recipient_dao.list_all() if x["id"] == rid), None)
            if r:
                members.append(r)
        return members

    def configure_sender(self, sender_email: str, app_password: str) -> bool:
        logger.info(f"[CONFIG] Configurando remetente: {sender_email}")
        try:
            self.controller = EmailController(app_password, sender_email)
            logger.info("[OK] Remetente configurado com sucesso")
            return True
        except Exception as e:
            logger.error(f"[ERRO] Erro ao configurar remetente: {e}")
            raise EmailServiceError(f"Erro ao configurar remetente: {e}")

    # ------------------------
    # Recipients CRUD via DAO
    # ------------------------
    def add_recipient(self, address: str, groupId: int = 0) -> Dict[str, Any]:
        try:
            rec = self.recipient_dao.add(address, groupId)
            logger.info(f"[SERVICE] Recipient added: {address}")

            # Sincronizar com o DAO de grupos: se o recipient foi criado com groupId,
            # garantir que o grupo contenha o id do recipient na sua lista.
            if groupId and rec and isinstance(rec, dict) and rec.get("id") is not None:
                try:
                    # add_recipient_to_group checa duplicatas internamente
                    self.group_dao.add_recipient_to_group(groupId, rec["id"])
                except Exception as grp_err:
                    logger.warning(f"[WARN] Falha ao associar recipient {rec.get('id')} ao grupo {groupId}: {grp_err}")

            return rec
        except Exception as e:
            logger.error(f"[ERRO] Erro ao adicionar destinatario: {e}")
            raise EmailServiceError(f"Erro ao adicionar destinatario: {e}")

    def list_recipients(self) -> List[Dict[str, Any]]:
        return self.recipient_dao.list_all()


    def process_recipient_file(self, file_path: str) -> List[str]:
        logger.info(f"[FILE] Processando arquivo: {file_path}")
        try:
            emails = self.recipient_dao.extract_emails_from_file(file_path)
            if not emails:
                logger.warning("[WARN] Nenhum email valido encontrado no arquivo")
                raise EmailServiceError("Nenhum email válido encontrado no arquivo")
            return emails
        except EmailServiceError:
            raise
        except Exception as e:
            logger.error(f"[ERRO] Erro ao processar arquivo: {e}")
            raise EmailServiceError(f"Erro ao processar arquivo: {e}")

    # ------------------------
    # Senders CRUD via DAO
    # ------------------------
    def add_sender(self, address: str, app_password: str) -> Dict[str, Any]:
        try:
            sender = self.sender_dao.add(address, app_password)
            logger.info(f"[SERVICE] Sender persisted: {address}")
            return sender
        except Exception as e:
            logger.error(f"[ERRO] Erro ao adicionar remetente: {e}")
            raise EmailServiceError(f"Erro ao adicionar remetente: {e}")

    def list_senders(self) -> List[Dict[str, Any]]:
        return self.sender_dao.list_all()

    def delete_sender(self, sender_id: int):
        try:
            return self.sender_dao.delete(sender_id)
        except Exception as e:
            logger.error(f"[ERRO] Erro ao deletar remetente: {e}")
            raise EmailServiceError(f"Erro ao deletar remetente: {e}")

    def send_bulk_emails(self, recipients: List[str], subject: str, body: str, attachments: List[str] = None) -> Dict[str, Any]:
        logger.info(f"[EMAIL] Iniciando envio em massa para {len(recipients)} destinatarios")
        if not self.controller:
            logger.error("[ERRO] Remetente nao configurado")
            raise EmailServiceError("Remetente não configurado")
        try:
            success = self.controller.sendMassEmails(recipients, subject, body, attachments)
            return {
                'success': success,
                'recipients_count': len(recipients),
                'attachments_count': len(attachments) if attachments else 0,
                'message': 'Emails enviados com sucesso' if success else 'Falha no envio'
            }
        except Exception as e:
            logger.error(f"[ERRO] Erro ao enviar emails: {e}")
            raise EmailServiceError(f"Erro ao enviar emails: {e}")

