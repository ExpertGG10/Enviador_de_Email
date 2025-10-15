from PySide6.QtWidgets import QDialog, QMessageBox
from gui.dialogs.ui_edit_recipient import Ui_Dialog_Edit_Recipient
from utils.validators import validate_email


class EditRecipientDialog(QDialog):
    def __init__(self, parent=None, email=''):
        super().__init__(parent)
        self.ui = Ui_Dialog_Edit_Recipient()
        self.ui.setupUi(self)
        self.ui.line_email.setText(email)
        self.ui.buttonBox.accepted.connect(self.on_accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def on_accept(self):
        email = self.ui.line_email.text().strip()
        if not email:
            QMessageBox.warning(self, "Validação", "Email obrigatório")
            return
        if not validate_email(email):
            QMessageBox.warning(self, "Validação", "Email inválido")
            return
        self.result = {'email': email}
        self.accept()
