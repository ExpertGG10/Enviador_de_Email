import sys
import logging
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from gui.main_window import MainWindow
from utils.util_arquivos import obterCaminhoBase, juntarCaminhos, checarArquivoExiste


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('email_sender_debug.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

def main():
    """Função principal para executar a aplicação."""
    logger.info("[START] Iniciando aplicacao Email Sender...")
    print("=" * 50)
    print("INICIANDO EMAIL SENDER")
    print("=" * 50)
    
    try:
        app = QApplication(sys.argv)
        logger.debug("[OK] QApplication criado")

        iconPath = juntarCaminhos(obterCaminhoBase(), "static/images/icon.ico")
        try:
            if checarArquivoExiste(iconPath):
                app.setWindowIcon(QIcon(iconPath))
                logger.debug("[OK] Icone definido com sucesso")
            else:
                logger.warning("[WARN] Arquivo de icone nao encontrado")
        except Exception:
            logger.error("[ERRO] Falha ao definir icone")
        
        # Configurar aplicação
        app.setApplicationName("Email Sender")
        app.setApplicationVersion("1.0")
        app.setOrganizationName("Rio Software")
        logger.debug("[OK] Configuracoes da aplicacao definidas")
        
        # Criar e mostrar janela principal
        logger.info("[UI] Criando janela principal...")
        window = MainWindow()
        logger.info("[OK] Janela principal criada")
        
        logger.info("[UI] Exibindo janela...")
        window.show()
        logger.info("[OK] Aplicacao iniciada com sucesso!")
        print("[OK] Aplicacao iniciada com sucesso!")
        print("Email Sender esta rodando...")
        print("=" * 50)
        
        sys.exit(app.exec())
        
    except Exception as e:
        logger.error(f"[ERRO] Erro fatal na inicializacao: {e}")
        print(f"[ERRO FATAL]: {e}")
        print("=" * 50)
        raise

if __name__ == "__main__":
    main()