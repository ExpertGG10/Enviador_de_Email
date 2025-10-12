import pandas as pd
import re
import logging

logger = logging.getLogger(__name__)

class EmailDao:
    def __init__(self, filePath: str):
        """
        Classe para extrair emails de arquivos Excel ou CSV.
        
        params:
        - filePath (str): Caminho para o arquivo Excel ou CSV.
        """
        self.filePath = filePath

    def getEmails(self) -> list[str]:
        logger.info(f"[FILE] Lendo arquivo: {self.filePath}")
        try:
            if self.filePath.endswith(('.xls', '.xlsx')):
                logger.debug("[EXCEL] Lendo arquivo Excel...")
                df = pd.read_excel(self.filePath)
                logger.debug(f"[DATA] DataFrame criado com {len(df)} linhas e {len(df.columns)} colunas")
            elif self.filePath.endswith('.csv'):
                logger.debug("[CSV] Lendo arquivo CSV...")
                df = pd.read_csv(self.filePath)
                logger.debug(f"[DATA] DataFrame criado com {len(df)} linhas e {len(df.columns)} colunas")
            else:
                logger.error(f"[ERRO] Formato nao suportado: {self.filePath}")
                raise ValueError("Formato de arquivo não suportado. Use .xlsx, .xls ou .csv.")
        except FileNotFoundError:
            logger.error(f"[ERRO] Arquivo nao encontrado: {self.filePath}")
            raise FileNotFoundError(f"Erro: O arquivo '{self.filePath}' não foi encontrado.")
        except Exception as e:
            logger.error(f"[ERRO] Erro ao ler arquivo: {e}")
            raise Exception(f"Erro ao ler o arquivo: {e}")

        regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        logger.debug(f"[REGEX] Regex para emails: {regexEmail}")
        
        emails = []
        logger.debug(f"[PROCESS] Processando {len(df.columns)} colunas...")

        for column in df.columns:
            logger.debug(f"[COLUMN] Processando coluna: {column}")
            for item in df[column]:
                if isinstance(item, str):
                    foundEmails = re.findall(regexEmail, item)
                    if foundEmails:
                        logger.debug(f"[EMAIL] Emails encontrados em '{item[:50]}...': {foundEmails}")
                    emails.extend(foundEmails)
        
        emails = list(set(emails))
        logger.info(f"[EMAIL] Total de emails unicos encontrados: {len(emails)}")
        logger.debug(f"[EMAIL] Emails: {emails[:10]}{'...' if len(emails) > 10 else ''}")

        return emails