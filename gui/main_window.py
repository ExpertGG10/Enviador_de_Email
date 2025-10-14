import sys
import os
import csv
import logging
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QProgressDialog, QLineEdit, QDialog
)
from PySide6.QtCore import QThread, Signal, Qt

from gui.dialogs.ui_adicionar_remetente import Ui_Dialog_Adicionar_Remetente

# Configurar logging para debug
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('email_sender_debug.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

# Configurar encoding para Windows
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Adicionar o diretório raiz ao path para importações
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
logger.debug(f"Adicionado ao sys.path: {os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}")

try:
    from gui.ui_mainwindow import Ui_MainWindow
    logger.debug("[OK] Importacao Ui_MainWindow bem-sucedida")
except ImportError as e:
    logger.error(f"[ERRO] Erro ao importar Ui_MainWindow: {e}")
    raise


try:
    from gui.dialogs.ui_adicionar_remetente import Ui_Dialog_Adicionar_Remetente
    logger.debug("[OK] Importacao Ui_MainWindow bem-sucedida")
except ImportError as e:
    logger.error(f"[ERRO] Erro ao importar Ui_MainWindow: {e}")
    raise


try:
    from core.email_service import EmailService
    logger.debug("[OK] Importacao EmailService bem-sucedida")
except ImportError as e:
    logger.error(f"[ERRO] Erro ao importar EmailService: {e}")
    raise

try:
    from utils.exceptions import EmailServiceError
    from utils.validators import validate_required_fields, validate_file_extension
    logger.debug("[OK] Importacoes de utils bem-sucedidas")
except ImportError as e:
    logger.error(f"[ERRO] Erro ao importar utils: {e}")
    raise

# Caso você tenha colado a classe Ui_MainWindow no MESMO arquivo deste código,
# mantenha a importação acima comentada e garanta que a classe Ui_MainWindow
# está definida antes desta classe MainWindow.

# ----------------------------
# Exemplo assume que Ui_MainWindow já está definido/importado
# ----------------------------

class EmailWorker(QThread):
    """Thread para envio de emails em background."""
    progress = Signal(int)
    finished = Signal(bool, str)
    
    def __init__(self, service, recipients, subject, body, attachments=None):
        super().__init__()
        self.service = service
        self.recipients = recipients
        self.subject = subject
        self.body = body
        self.attachments = attachments or []
        logger.debug(f"[EMAIL] EmailWorker criado para {len(recipients)} destinatarios")
        if self.attachments:
            logger.debug(f"[ANEXO] {len(self.attachments)} anexo(s) incluidos")
    
    def run(self):
        logger.info(f"[ENVIO] Iniciando envio de emails para {len(self.recipients)} destinatarios")
        try:
            result = self.service.send_bulk_emails(self.recipients, self.subject, self.body, self.attachments)
            logger.info(f"[OK] Envio concluido com sucesso: {result['message']}")
            self.finished.emit(True, result['message'])
        except EmailServiceError as e:
            logger.error(f"[ERRO] Erro no envio de emails: {e}")
            self.finished.emit(False, str(e))
        except Exception as e:
            logger.error(f"[ERRO] Erro inesperado no envio: {e}")
            self.finished.emit(False, f"Erro inesperado: {e}")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        logger.info("[INIT] Inicializando MainWindow...")
        super().__init__(parent)

        # Instancia e configura a UI gerada pelo Qt Designer
        logger.debug("[UI] Configurando interface UI...")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        logger.debug("[OK] Interface UI configurada")

        # Serviço de email
        logger.debug("[EMAIL] Criando EmailService...")
        self.email_service = EmailService()
        logger.debug("[OK] EmailService criado")
        
        # Estado do app
        self.remetente = None
        self.remetente_password = None
        self.destinatarios = []
        self.anexos = []
        self.email_worker = None
        logger.debug("[OK] Estado inicial configurado")

        # Configurar placeholders
        self.ui.lineEdit.setPlaceholderText("Digite o assunto do e-mail")
        self.ui.textEdit.setPlaceholderText("Digite a mensagem do e-mail...")
        logger.debug("[OK] Placeholders configurados")

        # Conectar sinais
        self._connect_signals()
        logger.debug("[OK] Sinais conectados")
        
        # Configurar interface inicial
        self._setup_initial_ui()
        logger.info("[OK] MainWindow inicializada com sucesso")


    def _connect_signals(self):
        # Botões
        self.ui.pushButton.clicked.connect(self.on_informacoes_clicked)        # "Informações"
        self.ui.pushButton_2.clicked.connect(self.on_anexo_clicked)            # "Anexo"
        self.ui.pushButton_3.clicked.connect(self.on_enviar_clicked)           # "Enviar"

        # Ações de menu
        self.ui.actionRemetente.triggered.connect(self.on_adicionar_remetente_triggered)
        self.ui.actionDestinatario.triggered.connect(self.on_importar_csv_triggered)
    
    def _setup_initial_ui(self):
        """Configuração inicial da interface."""
        self.setWindowTitle("Email Sender - Rio Software")
        self.statusBar().showMessage("Pronto para enviar emails")
        
        # Desabilitar botão de envio até configurar remetente
        self.ui.pushButton_3.setEnabled(False)

    # ----------------------------
    # Placeholders dos botões
    # ----------------------------
    def on_informacoes_clicked(self):

        anexos_info = ""
        if self.anexos:
            anexos_info = f"\nArquivos anexos:\n" + "\n".join([f"- {os.path.basename(anexo)}" for anexo in self.anexos[:5]])
            if len(self.anexos) > 5:
                anexos_info += f"\n... e mais {len(self.anexos) - 5} arquivo(s)"

        info = ( """Como gerar a Senha de Aplicativo no Gmail:

     1.  Acesse sua Conta Google, 
     2.  Vá em Segurança e ative a Verificação em Duas Etapas.
     2.  Na mesma tela de Segurança, vá em "Senhas de app".
     3.  Gere uma nova senha e copie o código gerado""")

        QMessageBox.information(self, "Senha App", info)

    def on_anexo_clicked(self):
        arquivos, _ = QFileDialog.getOpenFileNames(self, "Selecionar arquivos para anexar")
        if arquivos:
            self.anexos.extend(arquivos)
            self.statusBar().showMessage(
                f"{len(arquivos)} anexo(s) adicionado(s). Total: {len(self.anexos)}", 4000
            )

    def on_enviar_clicked(self):
        """Envia emails usando o serviço de email."""
        # Validar dados
        assunto = (self.ui.lineEdit.text() or "").strip()
        corpo = (self.ui.textEdit.toHtml() or "").strip()
        
        # Validar campos obrigatórios
        errors = validate_required_fields(self.remetente, self.destinatarios, assunto, corpo)
        if errors:
            QMessageBox.warning(self, "Dados Inválidos", "\n".join(errors))
            return
        
        # Confirmar envio
        reply = QMessageBox.question(
            self, 
            "Confirmar Envio", 
            f"Enviar email para {len(self.destinatarios)} destinatário(s)?\n\n"
            f"Assunto: {assunto}\n"
            f"Destinatários: {', '.join(self.destinatarios[:3])}{'...' if len(self.destinatarios) > 3 else ''}",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply != QMessageBox.Yes:
            return
        
        # Configurar serviço se necessário
        if not self.email_service.controller:
            try:
                self.email_service.configure_sender(self.remetente, self.remetente_password)
            except EmailServiceError as e:
                QMessageBox.critical(self, "Erro de Configuração", str(e))
                return
        
        # Criar e configurar diálogo de progresso
        self.progress_dialog = QProgressDialog("Enviando emails...", "Cancelar", 0, len(self.destinatarios), self)
        self.progress_dialog.setWindowModality(Qt.WindowModality.WindowModal)
        self.progress_dialog.show()
        
        # Criar worker thread
        self.email_worker = EmailWorker(self.email_service, self.destinatarios, assunto, corpo, self.anexos)
        self.email_worker.finished.connect(self.on_email_sent)
        self.email_worker.start()
        
        # Desabilitar botão durante envio
        self.ui.pushButton_3.setEnabled(False)
        self.statusBar().showMessage("Enviando emails...")
    
    def on_email_sent(self, success, message):
        """Callback chamado quando envio de email termina."""
        self.progress_dialog.close()
        self.ui.pushButton_3.setEnabled(True)
        
        if success:
            QMessageBox.information(self, "Sucesso", f"Emails enviados com sucesso!\n\n{message}")
            self.statusBar().showMessage(f"Enviados para {len(self.destinatarios)} destinatários")
        else:
            QMessageBox.critical(self, "Erro no Envio", f"Falha ao enviar emails:\n{message}")
            self.statusBar().showMessage("Erro no envio de emails")

    # ----------------------------
    # Placeholders das ações de menu
    # ----------------------------
    def on_adicionar_remetente_triggered(self):
        """Abre o diálogo de Adicionar Remetente (Qt Designer) para configurar remetente e senha."""
        # Ajuste o caminho do import conforme sua estrutura de pastas:

        logger.info("[EMAIL] Iniciando configuracao de remetente...")

        dlg = QDialog()
        dlg.ui = Ui_Dialog_Adicionar_Remetente()
        dlg.ui.setupUi(dlg)


        while True:
            result = dlg.exec_()
            if result != QDialog.DialogCode.Accepted:
                logger.debug("[CANCEL] Configuracao de remetente cancelada pelo usuario")
                QMessageBox.information(self, "Remetente", "Configuração cancelada.")
                return

            email = dlg.ui.lineEdit.text().strip()
            password = dlg.ui.lineEdit_2.text().strip()

            # Checagens básicas
            if not email:
                logger.debug("[VALIDACAO] Email vazio")
                QMessageBox.warning(self, "Email Obrigatório", "Por favor, digite um email válido.")
                continue

            if not password:
                logger.debug("[VALIDACAO] Senha vazia")
                QMessageBox.warning(self, "Senha Obrigatória", "Por favor, digite a senha de aplicativo.")
                continue

            # Validação de email

            # Se chegou aqui, está válido
            self.remetente = email
            self.remetente_password = password
            logger.info(f"[OK] Remetente configurado: {self.remetente}")
            break

        # Habilitar botão de envio (conforme seu exemplo)
        try:
            self.ui.pushButton_3.setEnabled(True)
        except Exception:
            # Se a UI não tiver esse botão em algum contexto, não quebra a execução
            pass

        try:
            self.statusBar().showMessage(f"Remetente configurado: {self.remetente}", 3000)
        except Exception:
            pass

        QMessageBox.information(self, "Remetente", "Remetente configurado com sucesso.")

  
    def on_escrever_manual_triggered(self):
        email, ok = QInputDialog.getText(self, "Adicionar Destinatário", "E-mail do destinatário:")
        if ok and email.strip():
            self.destinatarios.append(email.strip())
            self.statusBar().showMessage(f"Destinatário adicionado: {email.strip()}", 3000)
        elif ok:
            QMessageBox.information(self, "Destinatários", "Nenhum e-mail informado.")

    def on_importar_csv_triggered(self):
        """Importa destinatários de arquivo Excel/CSV usando o DAO."""
        logger.info("[IMPORT] Iniciando importacao de destinatarios...")
        caminho, _ = QFileDialog.getOpenFileName(
            self,
            "Importar destinatarios",
            filter="Arquivos suportados (*.csv *.xlsx *.xls);;CSV (*.csv);;Excel (*.xlsx *.xls);;Todos os arquivos (*.*)"
        )
        if not caminho:
            logger.debug("[CANCEL] Importacao cancelada pelo usuario")
            return

        logger.info(f"[FILE] Arquivo selecionado: {caminho}")

        # Validar extensão do arquivo
        if not validate_file_extension(caminho):
            logger.warning(f"[ERRO] Formato de arquivo nao suportado: {caminho}")
            QMessageBox.warning(
                self, 
                "Formato nao suportado", 
                "Por favor, selecione um arquivo CSV (.csv) ou Excel (.xlsx, .xls)."
            )
            return

        logger.debug(f"[OK] Formato de arquivo valido: {caminho}")

        try:
            # Usar o DAO para processar o arquivo
            logger.debug("[PROCESS] Processando arquivo com EmailService...")
            emails = self.email_service.process_recipient_file(caminho)
            logger.info(f"[EMAIL] {len(emails)} emails encontrados no arquivo")
            
            # Adicionar emails únicos (evitar duplicatas)
            novos_emails = []
            for email in emails:
                if email not in self.destinatarios:
                    self.destinatarios.append(email)
                    novos_emails.append(email)
            
            logger.info(f"[EMAIL] {len(novos_emails)} novos emails adicionados")
            logger.info(f"[TOTAL] Total de destinatarios: {len(self.destinatarios)}")
            
            if novos_emails:
                QMessageBox.information(
                    self, 
                    "Importacao Concluida", 
                    f"{len(novos_emails)} novo(s) destinatario(s) importado(s).\n"
                    f"Total de destinatarios: {len(self.destinatarios)}\n\n"
                    f"Primeiros emails:\n{', '.join(novos_emails[:5])}"
                    f"{'...' if len(novos_emails) > 5 else ''}"
                )
                self.statusBar().showMessage(f"{len(self.destinatarios)} destinatarios carregados")
            else:
                logger.info("[INFO] Nenhum email novo encontrado")
                QMessageBox.information(
                    self, 
                    "Nenhum email novo", 
                    "Todos os emails do arquivo ja estavam na lista de destinatarios."
                )
                
        except EmailServiceError as e:
            logger.error(f"[ERRO] Erro na importacao: {e}")
            QMessageBox.critical(self, "Erro na Importacao", str(e))
        except Exception as e:
            logger.error(f"[ERRO] Erro inesperado na importacao: {e}")
            QMessageBox.critical(self, "Erro Inesperado", f"Ocorreu um erro inesperado:\n{e}")


def main():
    """Função principal para executar a aplicação."""
    logger.info("[START] Iniciando aplicacao Email Sender...")
    print("=" * 50)
    print("INICIANDO EMAIL SENDER")
    print("=" * 50)
    
    try:
        app = QApplication(sys.argv)
        logger.debug("[OK] QApplication criado")
        
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
