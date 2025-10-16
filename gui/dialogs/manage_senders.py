from PySide6.QtWidgets import QDialog, QMessageBox, QListWidget, QListWidgetItem
from gui.dialogs.ui_crud import Ui_Dialog_Manage


class ManageSendersDialog(QDialog):
    def __init__(self, email_service, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_Manage()
        self.ui.setupUi(self)
        self.email_service = email_service
        self._connect()
        self.reload()
        self.selected_sender = None

    def _connect(self):
        self.ui.btn_add.clicked.connect(self.on_add)
        self.ui.btn_remove.clicked.connect(self.on_delete)
        self.ui.btn_select.clicked.connect(self.on_select)

    def reload(self):
        # Usar QListWidget para listar apenas os emails
        if not hasattr(self.ui, 'list_widget'):
            self.ui.list_widget = QListWidget(self)
            self.ui.verticalLayout.addWidget(self.ui.list_widget)
        lst = self.ui.list_widget
        lst.clear()
        senders = self.email_service.list_senders()
        for s in senders:
            lst.addItem(QListWidgetItem(s['address']))

    def on_add(self):
        from gui.dialogs.ui_adicionar_remetente import Ui_Dialog_Adicionar_Remetente
        import logging
        logger = logging.getLogger(__name__)
        logger.info("[EMAIL] Iniciando configuracao de remetente...")

        dlg = QDialog(self)
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

            # Adiciona na database
            sender = self.email_service.add_sender(email, password)
            logger.info(f"[OK] Remetente configurado e salvo: {sender['address']} (id={sender['id']})")
            QMessageBox.information(self, "Remetente", f"Remetente '{email}' adicionado com sucesso.")
            self.reload()
            break

    def on_delete(self):
        lst = getattr(self.ui, 'list_widget', None)
        if not lst:
            return
        row = lst.currentRow()
        if row < 0:
            return
        email = lst.item(row).text()
        senders = self.email_service.list_senders()
        s = next((x for x in senders if x['address'] == email), None)
        if s:
            self.email_service.delete_sender(s['id'])
            QMessageBox.information(self, "Remetente", f"Remetente '{email}' removido com sucesso.")
            self.reload()

    def on_select(self):
        lst = getattr(self.ui, 'list_widget', None)
        if not lst:
            return
        row = lst.currentRow()
        if row < 0:
            return
        email = lst.item(row).text()
        senders = self.email_service.list_senders()
        s = next((x for x in senders if x['address'] == email), None)
        if s:
            try:
                self.email_service.configure_sender(s['address'], s['appPassword'])
                self.selected_sender = s['address']
                self.selected_password = s['appPassword']
                QMessageBox.information(self, "Remetente", f"Remetente '{email}' selecionado com sucesso.")
                self.accept()
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Falha ao configurar remetente: {e}")
            print(f"[SELECT] Falha ao configurar remetente {email}: {e}")
            QMessageBox.critical(self, "Erro", f"Falha ao configurar remetente: {e}")
