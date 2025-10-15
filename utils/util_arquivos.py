from pathlib import Path

import os
import json
import sys
from typing import Optional, Dict

def obterCaminhoBase() -> str:
    """
    Retorna o caminho base do projeto.
    Se a aplicação estiver empacotada (usando PyInstaller), retorna o caminho
    do ambiente temporário. Caso contrário, retorna o diretório raiz do projeto.
    """
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    else:
        # Retorna o caminho para a pasta raiz do projeto.
        return os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

def criarDiretorioSistema(pastaSistema: str, nomeDiretorio: str) -> str:
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
    pastaSistema = pastaSistema.lower()
    pastasEspeciais = {
        'programdata': Path(os.getenv('ProgramData')),
        'appdata': Path(os.getenv('APPDATA') or os.path.expanduser('~')),
        'localappdata': Path(os.getenv('LOCALAPPDATA') or os.path.expanduser('~')),
        'temp': Path(os.getenv('TEMP') or os.path.expanduser('~')),
        'userprofile': Path(os.path.expanduser('~'))
    }

    if pastaSistema not in pastasEspeciais:
        raise ValueError(f"Pasta do sistema '{pastaSistema}' não reconhecida.")
    
    caminhoBase = pastasEspeciais[pastaSistema]
    caminhoCompleto = caminhoBase / nomeDiretorio
    try:
        caminhoCompleto.mkdir(parents=True, exist_ok=True)
        return str(caminhoCompleto)
    except Exception as e:
        raise Exception(f"Erro ao criar diretório '{caminhoCompleto}': {e}")

def carregarJson(caminhoArquivo: str) -> Dict:
    """
    Carrega dados de um arquivo JSON.
    
    Args:
        caminhoArquivo (str): O caminho para o arquivo JSON.
    
    Returns:
        dict: O conteúdo do arquivo como um dicionário, ou um dicionário vazio em caso de erro.
    """
    try:
        with open(caminhoArquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read().strip()
            if conteudo:
                return json.loads(conteudo)
    except Exception:
        pass
    return {}

def salvarJson(caminhoArquivo: str, dados: Dict):
    """
    Salva dados em um arquivo JSON.

    Args:
        caminhoArquivo (str): O caminho para o arquivo onde os dados serão salvos.
        dados (dict): O dicionário de dados a ser salvo.

    Raises:
        Exception: Se ocorrer um erro durante a escrita do arquivo.
    """
    diretorio = os.path.dirname(caminhoArquivo)
    try:
        os.makedirs(diretorio, exist_ok=True)
        with open(caminhoArquivo, 'wb') as f:
            data = json.dumps(dados, indent=4, ensure_ascii=False).encode('utf-8')
            f.write(data)
    except Exception as e:
        raise Exception(f"Erro ao salvar JSON no arquivo '{caminhoArquivo}': {e}")

def juntarCaminhos(diretorio: str, arquivo: str) -> str:
    """
    Junta um diretório e um nome de arquivo para formar um caminho completo.
    """
    return os.path.join(diretorio, arquivo)

def criarCopiaArquivo(origem: str, destino: str):
    """
    Cria uma cópia de um arquivo.

    Args:
        origem (str): O caminho do arquivo de origem.
        destino (str): O caminho onde a cópia será salva.

    Raises:
        Exception: Se ocorrer um erro durante a criação da cópia.
    """
    try:
        with open(origem, 'rb') as arqOrig:
            dados = arqOrig.read()
        with open(destino, 'wb') as arqDest:
            arqDest.write(dados)
    except Exception as e:
        raise Exception(f"Erro ao criar cópia do arquivo de '{origem}' para '{destino}': {e}")

def checarArquivoExiste(caminhoArquivo: str) -> bool:
    """
    Verifica se um arquivo existe no caminho especificado.
    """
    return os.path.isfile(caminhoArquivo)

def checarDiretorioExiste(caminhoDiretorio: str) -> bool:
    """
    Verifica se um diretório existe no caminho especificado.
    """
    return os.path.isdir(caminhoDiretorio)

def checarPastaUnc(caminho: Optional[str]) -> bool:
    """
    Verifica se um caminho corresponde a uma pasta UNC (rede).
    """
    if not caminho:
        return False
    return caminho.startswith("\\\\") or caminho.startswith("//")