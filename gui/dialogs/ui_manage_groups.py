from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QPushButton, QDialog, QWidget, QTabWidget
)


class Ui_Dialog_Manage_Groups(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 420)
        self.verticalLayout = QVBoxLayout(Dialog)

        self.title = QLabel("Gerenciar Grupos de Destinatários")
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)

        # Abas para grupos
        self.tabs = QTabWidget(Dialog)
        self.tabs.setObjectName("tabs")
        self.verticalLayout.addWidget(self.tabs)

        # Rodapé com CRUD de grupos
        footer = QWidget(Dialog)
        f_layout = QHBoxLayout(footer)
        self.btn_group_add = QPushButton("Adicionar Grupo")
        self.btn_group_edit = QPushButton("Editar Grupo")
        self.btn_group_delete = QPushButton("Remover Grupo")
        f_layout.addWidget(self.btn_group_add)
        f_layout.addWidget(self.btn_group_edit)
        f_layout.addWidget(self.btn_group_delete)
        f_layout.addStretch(1)
        self.verticalLayout.addWidget(footer)
