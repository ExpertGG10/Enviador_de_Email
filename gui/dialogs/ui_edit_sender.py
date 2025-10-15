from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox


class Ui_Dialog_Edit_Sender(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 140)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.label = QLabel("Email:")
        self.verticalLayout.addWidget(self.label)
        self.line_email = QLineEdit(Dialog)
        self.verticalLayout.addWidget(self.line_email)
        self.label2 = QLabel("Senha de app:")
        self.verticalLayout.addWidget(self.label2)
        self.line_password = QLineEdit(Dialog)
        self.line_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.verticalLayout.addWidget(self.line_password)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.verticalLayout.addWidget(self.buttonBox)
