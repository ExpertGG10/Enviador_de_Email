class RecipientModel:
    def __init__(self, recipientId: int, address: str, groupId: int):
        self.recipientId = recipientId
        self.groupId = groupId
        self.address = address