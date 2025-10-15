import os
import logging
from typing import List, Dict, Any, Optional

from dao.email_dao import EmailDao
from utils.util_arquivos import carregarJson, salvarJson, obterCaminhoBase, juntarCaminhos, checarArquivoExiste

logger = logging.getLogger(__name__)


class RecipientDao:
    """DAO para gerenciar destinatários com persistência em JSON."""

    def __init__(self, path: Optional[str] = None):
        base = obterCaminhoBase()
        self.path = path or juntarCaminhos(base, "data/recipients.json")
        self._data = {"next_id": 1, "recipients": []}
        self._load()

    def _load(self):
        data = carregarJson(self.path)
        if data:
            self._data = {
                "next_id": data.get("next_id", 1),
                "recipients": data.get("recipients", []),
            }

    def _save(self):
        salvarJson(self.path, self._data)

    def list_all(self) -> List[Dict[str, Any]]:
        return list(self._data["recipients"])

    def find_by_email(self, address: str) -> Optional[Dict[str, Any]]:
        for r in self._data["recipients"]:
            if r["address"].lower() == address.lower():
                return r
        return None

    def add(self, address: str, groupId: int = 0) -> Dict[str, Any]:
        existing = self.find_by_email(address)
        if existing:
            return existing
        new_id = self._data["next_id"]
        rec = {"id": new_id, "address": address, "groupId": groupId}
        self._data["recipients"].append(rec)
        self._data["next_id"] += 1
        self._save()
        logger.info(f"[DAO] Added recipient: {address} (id={new_id})")
        return rec

    def update(self, recipient_id: int, address: Optional[str] = None, groupId: Optional[int] = None) -> Dict[str, Any]:
        for r in self._data["recipients"]:
            if r["id"] == recipient_id:
                if address is not None:
                    r["address"] = address
                if groupId is not None:
                    r["groupId"] = groupId
                self._save()
                return r
        raise ValueError("Recipient not found")

    def delete(self, recipient_id: int) -> bool:
        before = len(self._data["recipients"])
        self._data["recipients"] = [r for r in self._data["recipients"] if r["id"] != recipient_id]
        if len(self._data["recipients"]) < before:
            self._save()
            logger.info(f"[DAO] Deleted recipient id={recipient_id}")
            return True
        return False

    def extract_emails_from_file(self, file_path: str) -> List[str]:
        if not checarArquivoExiste(file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
        email_dao = EmailDao(file_path)
        emails = email_dao.getEmails()
        return [e.lower() for e in sorted(set(emails))]
