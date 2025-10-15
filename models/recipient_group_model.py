from typing import List


class RecipientGroupModel:
    def __init__(self, groupId: int, name: str, recipients: List[int] | None = None):
        """
        Representa um grupo de destinatários.

        - groupId: id do grupo
        - name: nome do grupo
        - recipients: lista de recipient ids pertencentes ao grupo
        """
        self.groupId = groupId
        self.name = name
        self.recipients = recipients or []
