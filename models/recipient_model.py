class RecipientModel:
    """
    Model representing an email recipient.
    Args:
        recipient_id (int): Unique identifier for the recipient.
        address (str): Email address of the recipient.
        group_id (int): Group ID to which the recipient belongs.
    """
    def __init__(self, recipient_id: int = None, address: str = None, group_id: int = None):
        self.recipient_id = recipient_id
        self.group_id = group_id
        self.address = address