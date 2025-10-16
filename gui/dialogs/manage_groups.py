
from PySide6.QtWidgets import QDialog, QMessageBox, QListWidget, QListWidgetItem, QInputDialog, QFileDialog
from gui.dialogs.ui_crud import Ui_Dialog_Manage



class ManageGroupsDialog(QDialog):
    def __init__(self, email_service, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_Manage()
        self.ui.setupUi(self, titleText="Gerenciar Grupos de Destinatários")
        self.email_service = email_service
        self._connect()
        self.reload()
        self.selected_group = None

    def _connect(self):
        self.ui.btn_add.clicked.connect(self.on_add_group)
        self.ui.btn_remove.clicked.connect(self.on_delete_group)
        self.ui.btn_select.clicked.connect(self.on_select_group)

    def reload(self):
        # Exibe apenas nomes dos grupos em QListWidget
        lst = self.ui.list_widget
        lst.clear()
        groups = self.email_service.list_groups()
        for g in groups:
            lst.addItem(QListWidgetItem(g['name']))



    def on_add_group(self):
        name, ok = QInputDialog.getText(self, "Adicionar Grupo", "Nome do grupo:")
        if ok and name:
            # Adiciona grupo e solicita arquivo de destinatários
            group = self.email_service.add_group(name)
            path, _ = QFileDialog.getOpenFileName(self, "Selecionar arquivo", filter="Arquivos suportados (*.csv *.xlsx *.xls)")
            if path:
                emails = self.email_service.process_recipient_file(path)
                for e in emails:
                    rec = self.email_service.add_recipient(e, groupId=group['id'])
                    self.email_service.add_recipient_to_group(rec['id'], group['id'])
            self.reload()
            
    def on_delete_group(self):
        lst = self.ui.list_widget
        row = lst.currentRow()
        if row < 0:
            return
        group_name = lst.item(row).text()
        grp = next((g for g in self.email_service.list_groups() if g['name'] == group_name), None)
        if not grp:
            return
        self.email_service.delete_group(grp['id'])
        self.reload()

    # Removido: não há mais ações individuais de destinatários


    def on_select_group(self):
        lst = self.ui.list_widget
        row = lst.currentRow()
        if row < 0:
            return
        group_name = lst.item(row).text()
        grp = next((g for g in self.email_service.list_groups() if g['name'] == group_name), None)
        if not grp:
            return
        members = self.email_service.list_group_recipients(grp['id'])
        emails = [m['address'] for m in members]
        self.selected_group_emails = emails
        self.selected_group = grp['name']
        self.accept()
