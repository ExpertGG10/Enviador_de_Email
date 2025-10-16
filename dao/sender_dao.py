import os
import logging
from typing import List, Dict, Any, Optional

from utils.util_arquivos import carregarJson, criarDiretorioSistema, salvarJson, juntarCaminhos

logger = logging.getLogger(__name__)


class SenderDao:
    """DAO para gerenciar remetentes com persistência em JSON."""

    def __init__(self, path: Optional[str] = None):
        base = criarDiretorioSistema('appdata', 'Enviador de Email')
        self.path = path or juntarCaminhos(base, "data/senders.json")
        self._data = {"next_id": 1, "senders": []}
        self._load()

    def _load(self):
        data = carregarJson(self.path)
        if data:
            self._data = {"next_id": data.get("next_id", 1), "senders": data.get("senders", [])}

    def _save(self):
        salvarJson(self.path, self._data)

    def list_all(self) -> List[Dict[str, Any]]:
        return list(self._data["senders"])

    def find_by_email(self, address: str) -> Optional[Dict[str, Any]]:
        for s in self._data["senders"]:
            if s["address"].lower() == address.lower():
                return s
        return None

    def add(self, address: str, appPassword: str) -> Dict[str, Any]:
        existing = self.find_by_email(address)
        if existing:
            if existing.get("appPassword") != appPassword:
                existing["appPassword"] = appPassword
                self._save()
            return existing
        new_id = self._data["next_id"]
        sender = {"id": new_id, "address": address, "appPassword": appPassword}
        self._data["senders"].append(sender)
        self._data["next_id"] += 1
        self._save()
        logger.info(f"[DAO] Added sender: {address} (id={new_id})")
        return sender

    def delete(self, sender_id: int) -> bool:
        before = len(self._data["senders"])
        self._data["senders"] = [s for s in self._data["senders"] if s["id"] != sender_id]
        if len(self._data["senders"]) < before:
            self._save()
            logger.info(f"[DAO] Deleted sender id={sender_id}")
            return True
        return False
