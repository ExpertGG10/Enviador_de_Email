import logging

from typing import List

from dao.recipient_group_dao import RecipientGroupDao
from dao.recipient_dao import RecipientDao

from models.recipient_model import RecipientModel
from models.recipient_group_model import RecipientGroupModel

from utils.exceptions import EmailServiceError

logger = logging.getLogger(__name__)


class RecipientGroupController:
    """
    Controller for managing recipient groups.

    Args:
        recipient_dao (RecipientDao): DAO for recipients.
        group_dao (RecipientGroupDao): DAO for recipient groups.
    """

    def __init__(self, recipient_dao: RecipientDao = None, group_dao: RecipientGroupDao = None):
        self.recipient_dao = recipient_dao or RecipientDao()
        self.group_dao = group_dao or RecipientGroupDao()

        logger.info("[INIT] RecipientGroupController initialized")

    def add_group(self, name: str) -> RecipientGroupModel:
        """
        Add a new recipient group.

        Args:
            name (str): Name of the group.
        Returns:
            RecipientGroupModel: The added group data.
        """

        try:
            group = RecipientGroupModel(name=name)

            grp = self.group_dao.add(group)

            logger.info(f"[SERVICE] Group added: {name}")

            return grp
        except Exception as e:
            logger.error(f"[ERRO] Erro ao adicionar grupo: {e}")
            raise EmailServiceError(str(e))

    def list_groups(self) -> List[RecipientGroupModel]:
        """
        List all recipient groups.

        Returns:
            List[RecipientGroupModel]: List of recipient groups.
        """
        return self.group_dao.list_all()

    def delete_group(self, group_id: int) -> bool:
        """
        Delete a recipient group.

        Args:
            group_id (int): ID of the group to delete.
        Returns:
            bool: True if deleted, False otherwise.
        """
        try:
            deleted = self.group_dao.delete(group_id)
            if deleted:
                for r in self.recipient_dao.list_all():
                    if r.group_id == group_id:
                        try:
                            r.group_id = 0
                            self.recipient_dao.update(r)
                        except Exception:
                            logger.warning(f"[WARN] Falha ao resetar group_id do recipient {r.recipient_id}")
                logger.info(f"[SERVICE] Grupo {group_id} deletado e membros atualizados")
            return deleted
        except Exception as e:
            logger.error(f"[ERRO] Erro ao deletar grupo: {e}")

            raise EmailServiceError(str(e))

    def add_recipient_to_group(self, recipient_id: int, group_id: int) -> bool:
        """
        Add a recipient to a group.

        Args:
            recipient_id (int): ID of the recipient to add.
            group_id (int): ID of the group.
        Returns:
            bool: True if added, False otherwise.
        """
        try:
            recipient = RecipientModel(recipient_id=recipient_id, group_id=group_id)

            self.recipient_dao.update(recipient)
            self.group_dao.add_recipient_to_group(group_id, recipient_id)

            return True
        except Exception as e:
            logger.error(f"[ERRO] Erro ao adicionar recipient {recipient_id} ao grupo {group_id}: {e}")
            raise EmailServiceError(str(e))


    def list_group_recipients(self, group_id: int) -> List[RecipientModel]:
        """
        List all recipients in a group.

        Args:
            group_id (int): ID of the group.
        Returns:
            List[RecipientModel]: List of recipients in the group.
        """

        grp = self.group_dao.find_by_id(group_id)

        if not grp:
            raise EmailServiceError("Grupo não encontrado")
        members = []

        for recipient in self.recipient_dao.list_all():
            if recipient.recipient_id in grp.recipients:
                members.append(recipient)
        return members

    