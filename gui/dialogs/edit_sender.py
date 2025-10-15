from PySide6.QtWidgets import QDialog, QMessageBox
from gui.dialogs.ui_edit_sender import Ui_Dialog_Edit_Sender
from utils.validators import validate_email


class EditSenderDialog(QDialog):
    def __init__(self, parent=None, email='', password=''):
        super().__init__(parent)
        self.ui = Ui_Dialog_Edit_Sender()
        self.ui.setupUi(self)
        self.ui.line_email.setText(email)
        self.ui.line_password.setText(password)
        self.ui.buttonBox.accepted.connect(self.on_accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def on_accept(self):
        email = self.ui.line_email.text().strip()
        pwd = self.ui.line_password.text()
        if not email:
            QMessageBox.warning(self, "Validação", "Email obrigatório")
            return
        if not validate_email(email):
            QMessageBox.warning(self, "Validação", "Email inválido")
            return
        # retornar dados via atributos
        self.result = {'email': email, 'password': pwd}
        self.accept()
