import logging

from typing import List, Optional

from dao.base_dao import BaseDao

from models.recipient_group_model import RecipientGroupModel

logger = logging.getLogger(__name__)

class RecipientGroupDao(BaseDao):
    """
    DAO for managing recipient groups.

    Args:
        path (Optional[str]): Path to the JSON file for storing groups.
    
    """
    def __init__(self, path: Optional[str] = None):
        super().__init__(path, data_name="groups")

    def list_all(self) -> List[RecipientGroupModel]:
        """
        List all recipient groups.

        Returns:
            List[RecipientGroupModel]: List of recipient groups.
        """
        return [RecipientGroupModel(**g) for g in self._data[self.data_name]]

    def find_by_id(self, group_id: int) -> Optional[RecipientGroupModel]:
        """
        Find a group by its ID.

        Args:
            group_id (int): ID of the group to search for.
        Returns:
            Optional[Dict[str, Any]]: Group data if found, else None.
        """
        for g in self._data[self.data_name]:
            if g["group_id"] == group_id:
                return RecipientGroupModel(**g)
        return None

    def find_by_name(self, name: str) -> Optional[RecipientGroupModel]:
        """
        Find a group by its name.

        Args:
            name (str): Name of the group to search for.
        Returns:
            Optional[Dict[str, Any]]: Group data if found, else None.
        """
        for g in self._data[self.data_name]:
            if g["name"].lower() == name.lower():
                return g
        return None

    def add(self, group: RecipientGroupModel) -> RecipientGroupModel:
        """
        Add a new recipient group.

        Args:
            group (RecipientGroupModel): The group to add.
        Returns:
            RecipientGroupModel: The added group data.
        """
        existing = self.find_by_name(group.name)
        if existing:
            return existing
        
        new_id = self._data["next_id"]
        group.group_id = new_id

        self._data[self.data_name].append(group.__dict__)

        self._data["next_id"] += 1

        self._save()

        logger.info(f"[DAO] Added group: {group.name} (id={new_id})")
        
        return group

    def update(self, group: RecipientGroupModel) -> RecipientGroupModel:
        """
        Update an existing recipient group.

        Args:
            group (RecipientGroupModel): The group to update.

        Returns:
            RecipientGroupModel: The updated group data.
        """

        for g in self._data[self.data_name]:
            if g["group_id"] == group.group_id:
                if group.group_id is not None:
                    g["group_id"] = group.group_id
                if group.name is not None:
                    g["name"] = group.name
                if group.recipients is not None:
                    g["recipients"] = group.recipients
                self._save()

        logger.info(f"[DAO] Updated group id={group.group_id}")

        return group

    def delete(self, group_id: int) -> bool:
        """
        Delete a recipient group.

        Args:
            group_id (int): ID of the group to delete.
        Returns:
            bool: True if deleted, False otherwise.
        """

        before = len(self._data[self.data_name])

        self._data[self.data_name] = [
            g for g in self._data[self.data_name] if g["group_id"] != group_id
        ]

        if len(self._data[self.data_name]) < before:
            self._save()

            logger.info(f"[DAO] Deleted group id={group_id}")
            
            return True
        
        return False

    def add_recipient_to_group(self, group_id: int, recipient_id: int) -> bool:
        """
        Add a recipient to a group.

        Args:
            group_id (int): ID of the group.
            recipient_id (int): ID of the recipient to add.
        Returns:
            bool: True if added, False if already present.
        """
        
        g = self.find_by_id(group_id)
        if not g:
            raise ValueError("Group not found")
        
        if recipient_id not in g.recipients:
            g.recipients.append(recipient_id)

            self.update(g)

            self._save()

            logger.info(f"[DAO] Added recipient {recipient_id} to group {group_id}")
            
            return True
        return False

    def remove_recipient_from_group(self, group_id: int, recipient_id: int) -> bool:
        """
        Remove a recipient from a group.

        Args:
            group_id (int): ID of the group.
            recipient_id (int): ID of the recipient to remove.
        Returns:
            bool: True if removed, False if not found.
        """
        g = self.find_by_id(group_id)
        if not g:
            raise ValueError("Group not found")
        
        before = len(g.recipients)

        g.recipients = [
            rid for rid in g.recipients if rid != recipient_id
        ]

        if len(g.recipients) < before:
            self._save()

            logger.info(f"[DAO] Removed recipient {recipient_id} from group {group_id}")

            return True
        
        return False
