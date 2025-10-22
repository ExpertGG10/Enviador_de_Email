from typing import List

class RecipientGroupModel:
    """
    Model representing a group of recipients.

    Args:
        group_id (int): Unique identifier for the group. 
        name (str): Name of the group.
        recipients (List[int] | None): List of recipient IDs belonging to the group.
    """
    def __init__(self, group_id: int = None, name: str = None, recipients: List[int] | None = None):

        self.group_id = group_id
        self.name = name
        self.recipients = recipients or []
