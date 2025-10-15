import os
from PySide6.QtWidgets import (
    QDialog, QMessageBox, QTableWidget, QTableWidgetItem, QInputDialog, QFileDialog, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QHeaderView
)
from gui.dialogs.edit_recipient import EditRecipientDialog
from gui.dialogs.ui_manage_groups import Ui_Dialog_Manage_Groups


class ManageGroupsDialog(QDialog):
    def __init__(self, email_service, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_Manage_Groups()
        self.ui.setupUi(self)
        self.email_service = email_service
        self._connect()
        self.reload()

    def _connect(self):
        self.ui.btn_group_add.clicked.connect(self.on_add_group)
        self.ui.btn_group_edit.clicked.connect(self.on_edit_group)
        self.ui.btn_group_delete.clicked.connect(self.on_delete_group)
        self.ui.tabs.currentChanged.connect(lambda _: self.reload_tab())

    def reload(self):
        # Rebuild tabs without triggering currentChanged to avoid recursion
        self.ui.tabs.blockSignals(True)
        try:
            self.ui.tabs.clear()
            for g in self.email_service.list_groups():
                self._add_group_tab(g)
        finally:
            self.ui.tabs.blockSignals(False)

    def _add_group_tab(self, group):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        lbl = QLabel(f"Grupo: {group['name']}")
        layout.addWidget(lbl)

        table = QTableWidget()
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(['ID', 'Email'])
        # visual tweaks
        header = table.horizontalHeader()
        header.setStretchLastSection(True)
        table.setWordWrap(False)
        table.setAlternatingRowColors(True)
        layout.addWidget(table)

        # carregar membros
        members = self.email_service.list_group_recipients(group['id'])
        table.setRowCount(len(members))
        for i, m in enumerate(members):
            table.setItem(i, 0, QTableWidgetItem(str(m['id'])))
            table.setItem(i, 1, QTableWidgetItem(m['address']))
        table.resizeColumnsToContents()

        # botões internos
        btn_add_file = QPushButton("Adicionar em massa (arquivo)")
        btn_add_single = QPushButton("Adicionar Destinatário")
        btn_edit = QPushButton("Editar")
        btn_delete = QPushButton("Remover")
        btn_send = QPushButton("Selecionar para envio")
        # Compact button layout
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_add_file)
        btn_layout.addWidget(btn_add_single)
        btn_layout.addWidget(btn_edit)
        btn_layout.addWidget(btn_delete)
        btn_layout.addStretch(1)
        btn_layout.addWidget(btn_send)
        layout.addLayout(btn_layout)

        # Conexões
        btn_add_file.clicked.connect(lambda _, gid=group['id'], tbl=table: self.on_add_file(gid, tbl))
        btn_add_single.clicked.connect(lambda _, gid=group['id'], tbl=table: self.on_add_single(gid, tbl))
        btn_edit.clicked.connect(lambda _, gid=group['id'], tbl=table: self.on_edit_recipient(gid, tbl))
        btn_delete.clicked.connect(lambda _, gid=group['id'], tbl=table: self.on_delete_recipient(gid, tbl))
        btn_send.clicked.connect(lambda _, gid=group['id']: self.on_select_group_for_send(gid))

        self.ui.tabs.addTab(tab, group['name'])

    def reload_tab(self):
        # Atualiza somente a aba atualmente selecionada (não reconstrói todas as abas).
        idx = self.ui.tabs.currentIndex()
        if idx == -1:
            return

        # Obter o nome do grupo da aba selecionada
        group_name = self.ui.tabs.tabText(idx)
        grp = next((g for g in self.email_service.list_groups() if g['name'] == group_name), None)
        if not grp:
            return

        # Atualizar a tabela dentro da aba atual
        tab = self.ui.tabs.widget(idx)
        if not tab:
            return
        table = tab.findChild(QTableWidget)
        if table is None:
            return

        members = self.email_service.list_group_recipients(grp['id'])
        table.setRowCount(len(members))
        for i, m in enumerate(members):
            table.setItem(i, 0, QTableWidgetItem(str(m['id'])))
            table.setItem(i, 1, QTableWidgetItem(m['address']))
        table.resizeColumnsToContents()

    def on_add_group(self):
        name, ok = QInputDialog.getText(self, "Adicionar Grupo", "Nome do grupo:")
        if ok and name:
            self.email_service.add_group(name)
            self.reload()

    def on_edit_group(self):
        idx = self.ui.tabs.currentIndex()
        if idx == -1:
            return
        group_name = self.ui.tabs.tabText(idx)
        # localizar grupo por nome
        grp = next((g for g in self.email_service.list_groups() if g['name'] == group_name), None)
        if not grp:
            return
        name, ok = QInputDialog.getText(self, "Editar Grupo", "Nome:", text=grp['name'])
        if ok and name:
            self.email_service.update_group(grp['id'], name)
            self.reload()

    def on_delete_group(self):
        idx = self.ui.tabs.currentIndex()
        if idx == -1:
            return
        group_name = self.ui.tabs.tabText(idx)
        grp = next((g for g in self.email_service.list_groups() if g['name'] == group_name), None)
        if not grp:
            return
        self.email_service.delete_group(grp['id'])
        self.reload()

    def on_add_file(self, group_id: int, table: QTableWidget):
        path, _ = QFileDialog.getOpenFileName(self, "Selecionar arquivo", filter="Arquivos suportados (*.csv *.xlsx *.xls)")
        if not path:
            return
        emails = self.email_service.process_recipient_file(path)
        novos = []
        for e in emails:
            rec = self.email_service.add_recipient(e, groupId=group_id)
            novos.append(rec)
        # recarregar tabela
        self.reload()

    def on_add_single(self, group_id: int, table: QTableWidget):
        dlg = EditRecipientDialog(self)
        if dlg.exec_() == QDialog.DialogCode.Accepted:
            data = getattr(dlg, 'result', None)
            if data:
                rec = self.email_service.add_recipient(data['email'], groupId=group_id)
                self.email_service.add_recipient_to_group(rec['id'], group_id)
                self.reload()

    def on_edit_recipient(self, group_id: int, table: QTableWidget):
        row = table.currentRow()
        if row < 0:
            return
        rid = int(table.item(row, 0).text())
        current = table.item(row, 1).text()
        dlg = EditRecipientDialog(self, email=current)
        if dlg.exec_() == QDialog.DialogCode.Accepted:
            data = getattr(dlg, 'result', None)
            if data:
                self.email_service.update_recipient(rid, address=data['email'], groupId=group_id)
                self.reload()

    def on_delete_recipient(self, group_id: int, table: QTableWidget):
        row = table.currentRow()
        if row < 0:
            return
        rid = int(table.item(row, 0).text())
        self.email_service.delete_recipient(rid)
        self.reload()

    def on_select_group_for_send(self, group_id: int):
        # Obtém emails do grupo, guarda na instância e fecha o diálogo para o chamador
        members = self.email_service.list_group_recipients(group_id)
        emails = [m['address'] for m in members]
        self.selected_group_emails = emails
        # fechar com Accepted para o MainWindow capturar a seleção
        self.accept()
