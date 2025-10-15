from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox


class Ui_Dialog_Edit_Recipient(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 120)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.label = QLabel("Email:")
        self.verticalLayout.addWidget(self.label)
        self.line_email = QLineEdit(Dialog)
        self.verticalLayout.addWidget(self.line_email)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.verticalLayout.addWidget(self.buttonBox)
