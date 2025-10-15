from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidget, QTableWidgetItem
from gui.dialogs.ui_manage_senders import Ui_Dialog_Manage_Senders
from gui.dialogs.edit_sender import EditSenderDialog


class ManageSendersDialog(QDialog):
    def __init__(self, email_service, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_Manage_Senders()
        self.ui.setupUi(self)
        self.email_service = email_service
        self._connect()
        self.reload()

    def _connect(self):
        self.ui.btn_add.clicked.connect(self.on_add)
        self.ui.btn_edit.clicked.connect(self.on_edit)
        self.ui.btn_delete.clicked.connect(self.on_delete)
        self.ui.btn_select.clicked.connect(self.on_select)

    def reload(self):
        # substituir por tabela
        # se a tabela não existir ainda, cria-la
        if not hasattr(self.ui, 'table'):
            self.ui.table = QTableWidget(self)
            self.ui.table.setColumnCount(2)
            self.ui.table.setHorizontalHeaderLabels(['ID', 'Email'])
            self.ui.verticalLayout.addWidget(self.ui.table)
        table = self.ui.table
        senders = self.email_service.list_senders()
        table.setRowCount(len(senders))
        for i, s in enumerate(senders):
            table.setItem(i, 0, QTableWidgetItem(str(s['id'])))
            table.setItem(i, 1, QTableWidgetItem(s['address']))

    def on_add(self):
        dlg = EditSenderDialog(self)
        if dlg.exec_() == QDialog.DialogCode.Accepted:
            data = getattr(dlg, 'result', None)
            if data:
                self.email_service.add_sender(data['email'], data['password'])
                self.reload()

    def on_edit(self):
        table = getattr(self.ui, 'table', None)
        if not table:
            return
        row = table.currentRow()
        if row < 0:
            return
        sid = int(table.item(row, 0).text())
        email = table.item(row, 1).text()
        dlg = EditSenderDialog(self, email=email)
        if dlg.exec_() == QDialog.DialogCode.Accepted:
            data = getattr(dlg, 'result', None)
            if data:
                self.email_service.add_sender(data['email'], data['password'])
                self.reload()

    def on_delete(self):
        table = getattr(self.ui, 'table', None)
        if not table:
            return
        row = table.currentRow()
        if row < 0:
            return
        sid = int(table.item(row, 0).text())
        self.email_service.delete_sender(sid)
        self.reload()

    def on_select(self):
        table = getattr(self.ui, 'table', None)
        if not table:
            return
        row = table.currentRow()
        if row < 0:
            return
        sid = int(table.item(row, 0).text())
        senders = self.email_service.list_senders()
        s = next((x for x in senders if x['id'] == sid), None)
        if s:
            try:
                # configure sender in the service and store selection for caller
                self.email_service.configure_sender(s['address'], s.get('appPassword', ''))
                self.selected_sender = s['address']
                self.selected_password = s.get('appPassword', '')
                # close dialog and return Accepted to caller
                self.accept()
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Falha ao configurar remetente: {e}")
