import logging
from typing import List, Dict, Any, Optional


from dao.recipient_dao import RecipientDao
from dao.sender_dao import SenderDao
from dao.recipient_group_dao import RecipientGroupDao

from utils.exceptions import EmailServiceError

from controller.email_controller import EmailController
from controller.sender_controller import SenderController
from controller.recipient_controller import RecipientController
from controller.recipient_group_controller import RecipientGroupController

from models.sender_model import SenderModel

logger = logging.getLogger(__name__)


class EmailService:
    """
    Serviço central para gerenciar operações de email.
    Coordena entre DAOs, Controller e validações.
    """

    def __init__(self):
        self.recipient_dao = RecipientDao()
        self.sender_dao = SenderDao()
        self.group_dao = RecipientGroupDao()

        self.email_controller: Optional[EmailController] = None
        self.sender_controller = SenderController(self.sender_dao)
        self.recipient_controller = RecipientController(self.recipient_dao, self.group_dao)
        self.group_controller = RecipientGroupController(self.recipient_dao, self.group_dao)

    def configure_sender(self, sender: SenderModel) -> bool:
        logger.info(f"[CONFIG] Configurando remetente: {sender.address}")
        try:
            self.email_controller = EmailController(sender)
            logger.info("[OK] Remetente configurado com sucesso")
            return True
        except Exception as e:
            logger.error(f"[ERRO] Erro ao configurar remetente: {e}")
            raise EmailServiceError(f"Erro ao configurar remetente: {e}")
    

    

