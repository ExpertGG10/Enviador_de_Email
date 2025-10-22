from typing import Optional
from utils.files import load_json, create_system_directory, save_json, join_paths

class BaseDao:
    """
    Base DAO class for managing JSON-persisted data.

    Args:
        path (Optional[str]): Path to the JSON file for storing data.
        data_name (str): The key name in the JSON for the list of items.
    """
    def __init__(self, path: Optional[str] = None, data_name: str = ""):
        base = create_system_directory('appdata', 'Enviador de Email')
        self.path = path or join_paths(base, f"data/{data_name}.json")

        self.data_name = data_name

        self._data = {"next_id": 1, f"{data_name}": []}
        self._load()

    def _load(self):
        """
        Load data from JSON file.
        """
        data = load_json(self.path)
        if data:
            self._data = {"next_id": data.get("next_id", 1), f"{self.data_name}": data.get(f"{self.data_name}", [])}

    def _save(self):
        """
        Save data to JSON file.
        """
        save_json(self.path, self._data)