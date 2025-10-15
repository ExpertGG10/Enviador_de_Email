from typing import List, Dict, Any, Optional
import logging
import os

from utils.util_arquivos import carregarJson, salvarJson, obterCaminhoBase, juntarCaminhos

logger = logging.getLogger(__name__)


class RecipientGroupDao:
    """DAO para gerenciar grupos de destinatários com persistência em JSON."""

    def __init__(self, path: Optional[str] = None):
        base = obterCaminhoBase()
        self.path = path or juntarCaminhos(base, "data/groups.json")
        # Garantir diretório
        parent = os.path.dirname(self.path) or '.'
        os.makedirs(parent, exist_ok=True)
        self._data = {"next_id": 1, "groups": []}
        self._load()

    def _load(self):
        data = carregarJson(self.path)
        if data:
            self._data = {"next_id": data.get("next_id", 1), "groups": data.get("groups", [])}

    def _save(self):
        salvarJson(self.path, self._data)

    def list_all(self) -> List[Dict[str, Any]]:
        return list(self._data["groups"])

    def find_by_id(self, group_id: int) -> Optional[Dict[str, Any]]:
        for g in self._data["groups"]:
            if g["id"] == group_id:
                return g
        return None

    def find_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        for g in self._data["groups"]:
            if g["name"].lower() == name.lower():
                return g
        return None

    def add(self, name: str) -> Dict[str, Any]:
        existing = self.find_by_name(name)
        if existing:
            return existing
        new_id = self._data["next_id"]
        group = {"id": new_id, "name": name, "recipients": []}
        self._data["groups"].append(group)
        self._data["next_id"] += 1
        self._save()
        logger.info(f"[DAO] Added group: {name} (id={new_id})")
        return group

    def update(self, group_id: int, name: Optional[str] = None) -> Dict[str, Any]:
        g = self.find_by_id(group_id)
        if not g:
            raise ValueError("Group not found")
        if name is not None:
            g["name"] = name
        self._save()
        logger.info(f"[DAO] Updated group id={group_id}")
        return g

    def delete(self, group_id: int) -> bool:
        before = len(self._data["groups"])
        self._data["groups"] = [g for g in self._data["groups"] if g["id"] != group_id]
        if len(self._data["groups"]) < before:
            self._save()
            logger.info(f"[DAO] Deleted group id={group_id}")
            return True
        return False

    def add_recipient_to_group(self, group_id: int, recipient_id: int) -> bool:
        g = self.find_by_id(group_id)
        if not g:
            raise ValueError("Group not found")
        if recipient_id not in g["recipients"]:
            g["recipients"].append(recipient_id)
            self._save()
            logger.info(f"[DAO] Added recipient {recipient_id} to group {group_id}")
            return True
        return False

    def remove_recipient_from_group(self, group_id: int, recipient_id: int) -> bool:
        g = self.find_by_id(group_id)
        if not g:
            raise ValueError("Group not found")
        before = len(g["recipients"])
        g["recipients"] = [rid for rid in g["recipients"] if rid != recipient_id]
        if len(g["recipients"]) < before:
            self._save()
            logger.info(f"[DAO] Removed recipient {recipient_id} from group {group_id}")
            return True
        return False
