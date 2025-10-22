import logging

from typing import List

from dao.sender_dao import SenderDao

from models.sender_model import SenderModel

from utils.exceptions import EmailServiceError

logger = logging.getLogger(__name__)

class SenderController:
    """
    Controller for managing email senders.

    Args:
        sender_dao (SenderDao): DAO for sender data management.
    """

    def __init__(self, sender_dao: SenderDao = None):
        self.sender_dao = sender_dao or SenderDao()

        logger.info("[INIT] SenderController initialized")

    def add_sender(self, address: str, app_password: str) -> SenderModel:
        """
        Add a new sender.

        Args:
            address (str): Email address of the sender.
            app_password (str): App password for the sender email.

        Returns:
            SenderModel: The added sender data.
        """
        try:
            sender = SenderModel(address=address, app_password=app_password)

            sender = self.sender_dao.add(sender)

            logger.info(f"[SERVICE] Sender persisted: {address}")

            return sender
        except Exception as e:
            logger.error(f"[ERRO] Erro ao adicionar remetente: {e}")

            raise EmailServiceError(f"Erro ao adicionar remetente: {e}")

    def list_senders(self) -> List[SenderModel]:
        """
        List all email senders.

        Returns:
            List[SenderModel]: List of senders.
        """
        return self.sender_dao.list_all()

    def delete_sender(self, sender_id: int) -> bool:
        """
        Delete a sender by its ID.
        
        Args:
            sender_id (int): ID of the sender to delete.

        Returns:
            bool: True if the sender was deleted, False otherwise.
        """

        try:
            return self.sender_dao.delete(sender_id)
        except Exception as e:
            logger.error(f"[ERRO] Erro ao deletar remetente: {e}")

            raise EmailServiceError(f"Erro ao deletar remetente: {e}")
        
    