from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QPushButton, QDialog, QWidget
)


class Ui_Dialog_Manage_Senders(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 320)
        self.verticalLayout = QVBoxLayout(Dialog)

        self.title = QLabel("Gerenciar Remetentes")
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)

        self.list_widget = QListWidget(Dialog)
        self.list_widget.setObjectName("list_widget")
        self.verticalLayout.addWidget(self.list_widget)

        btn_row = QWidget(Dialog)
        btn_layout = QHBoxLayout(btn_row)
        self.btn_add = QPushButton("Adicionar")
        self.btn_edit = QPushButton("Editar")
        self.btn_delete = QPushButton("Remover")
        self.btn_select = QPushButton("Selecionar")
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_edit)
        btn_layout.addWidget(self.btn_delete)
        btn_layout.addStretch(1)
        btn_layout.addWidget(self.btn_select)
        self.verticalLayout.addWidget(btn_row)
