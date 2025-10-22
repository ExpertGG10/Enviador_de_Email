import os
import json
import sys

from pathlib import Path
from typing import Optional, Dict

def get_base_path() -> str:
    """
    Retorna o caminho base do projeto.
    Se a aplicação estiver empacotada (usando PyInstaller), retorna o caminho
    do ambiente temporário. Caso contrário, retorna o diretório raiz do projeto.
    """
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    # Return project root dir
    return os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

def add_to_sys_path(path: str):
    """
    Adiciona o caminho especificado ao sys.path se ainda não estiver presente.
    """
    abs_path = os.path.abspath(path)
    
    if abs_path not in sys.path:
        sys.path.insert(0, abs_path)

def create_system_directory(system_folder: str, directory_name: str) -> str:
    """
    Cria um diretório em uma pasta especial do sistema (ex: AppData, ProgramData).

    Args:
        pastaSistema (str): O nome da pasta do sistema (ex: 'appdata', 'programdata').
        nomeDiretorio (str): O nome do diretório a ser criado.
    
    Returns:
        str: O caminho completo para o diretório criado.
    
    Raises:
        ValueError: Se a pasta do sistema não for reconhecida.
        Exception: Se ocorrer um erro durante a criação do diretório.
    """
    system_folder = system_folder.lower()
    special_folders = {
        'programdata': Path(os.getenv('ProgramData') or os.getcwd()),
        'appdata': Path(os.getenv('APPDATA') or os.path.expanduser('~')),
        'localappdata': Path(os.getenv('LOCALAPPDATA') or os.path.expanduser('~')),
        'temp': Path(os.getenv('TEMP') or os.path.expanduser('~')),
        'userprofile': Path(os.path.expanduser('~'))
    }

    if system_folder not in special_folders:
        raise ValueError(f"Unknown system folder '{system_folder}'.")

    base_path = special_folders[system_folder]
    target = base_path / directory_name
    try:
        target.mkdir(parents=True, exist_ok=True)
        return str(target)
    except Exception as e:
        raise Exception(f"Error creating directory '{target}': {e}")

def load_json(file_path: str) -> Dict:
    """
    Carrega dados de um arquivo JSON.
    
    Args:
        caminhoArquivo (str): O caminho para o arquivo JSON.
    
    Returns:
        dict: O conteúdo do arquivo como um dicionário, ou um dicionário vazio em caso de erro.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                return json.loads(content)
    except Exception:
        pass
    return {}

def save_json(file_path: str, data: Dict):
    """
    Salva dados em um arquivo JSON.

    Args:
        caminhoArquivo (str): O caminho para o arquivo onde os dados serão salvos.
        dados (dict): O dicionário de dados a ser salvo.

    Raises:
        Exception: Se ocorrer um erro durante a escrita do arquivo.
    """
    directory = os.path.dirname(file_path)
    try:
        os.makedirs(directory, exist_ok=True)
        with open(file_path, 'wb') as f:
            payload = json.dumps(data, indent=4, ensure_ascii=False).encode('utf-8')
            f.write(payload)
    except Exception as e:
        raise Exception(f"Error saving JSON to '{file_path}': {e}")

def join_paths(directory: str, filename: str) -> str:
    """
    Junta um diretório e um nome de arquivo para formar um caminho completo.
    """
    return os.path.join(directory, filename)

def copy_file(src: str, dst: str):
    """
    Cria uma cópia de um arquivo.

    Args:
        origem (str): O caminho do arquivo de origem.
        destino (str): O caminho onde a cópia será salva.

    Raises:
        Exception: Se ocorrer um erro durante a criação da cópia.
    """
    try:
        with open(src, 'rb') as s:
            data = s.read()
        with open(dst, 'wb') as d:
            d.write(data)
    except Exception as e:
        raise Exception(f"Error copying file from '{src}' to '{dst}': {e}")

def file_exists(path: str) -> bool:
    """
    Verifica se um arquivo existe no caminho especificado.
    """
    return os.path.isfile(path)

def dir_exists(path: str) -> bool:
    """
    Verifica se um diretório existe no caminho especificado.
    """
    return os.path.isdir(path)

def is_unc_path(path: Optional[str]) -> bool:
    """
    Verifica se um caminho corresponde a uma pasta UNC (rede).
    """
    if not path:
        return False
    return path.startswith("\\\\") or path.startswith("//")

