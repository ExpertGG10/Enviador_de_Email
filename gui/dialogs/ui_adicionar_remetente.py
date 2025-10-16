# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'novo remetentebepsrZ.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog_Adicionar_Remetente(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(182, 166)
        Dialog.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Dialog.setStyleSheet(u"/* Estilo simples e unificado para um app b\u00e1sico (MainWindow > QSS)\n"
"   - Aplique classes via propriedade din\u00e2mica \"class\" no Qt Designer\n"
"   - Classes dispon\u00edveis:\n"
"     Bot\u00f5es: primary, secondary, danger, text\n"
"     Labels: title, subtitle, caption, muted\n"
"     Inputs: error, success\n"
"*/\n"
"\n"
"/* Base global */\n"
"QMainWindow, QWidget {\n"
"  background: #EAF6FE;\n"
"  color: #1f2937;            /* cinza-900 */\n"
"  font-family: \"Segoe UI\", \"Roboto\", \"Inter\", \"Noto Sans\", Arial, sans-serif;\n"
"  font-size: 10pt;\n"
"  selection-background-color: #2563eb;  /* azul-600 */\n"
"  selection-color: #ffffff;\n"
"}\n"
"\n"
"/* Tooltips (opcional) */\n"
"QToolTip {\n"
"  background-color: #111827; /* cinza-900 */\n"
"  color: #f9fafb;            /* cinza-50 */\n"
"  border: 1px solid #111827;\n"
"  padding: 4px 8px;\n"
"  border-radius: 6px;\n"
"}\n"
"\n"
"/* ---------------------------\n"
"   Labels (QLabel)\n"
"   --------------------------- */\n"
"QLabel {\n"
""
                        "  color: #312783; /* cinza-900 */\n"
"}\n"
"\n"
"/* ---------------------------\n"
"   Inputs (QLineEdit, QTextEdit, QPlainTextEdit)\n"
"   --------------------------- */\n"
"QLineEdit,\n"
"QTextEdit,\n"
"QPlainTextEdit {\n"
"  background: #ffffff;\n"
"  color: #111827;\n"
"  border: 1px solid rgb(0,0,63);  \n"
"  border-radius: 6px;\n"
"  padding: 6px 8px;\n"
"}\n"
"\n"
"/* ---------------------------\n"
"   Bot\u00f5es (QPushButton)\n"
"   --------------------------- */\n"
"QPushButton {\n"
"  background: #312783;           /* cinza-200 */\n"
"  color: #f0f0f0;                /* cinza-900 */\n"
"  border: 1px solid #d1d5db;     /* cinza-300 */\n"
"  border-radius: 6px;\n"
"  padding: 6px 12px;\n"
"  font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #2563fb;           /* leve escurecido */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #4583fb;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"  background: #f3f4f6;           /* cinza-100 */\n"
"  color: #9ca3af;                /* cinza-4"
                        "00 */\n"
"  border-color: #e5e7eb;         /* cinza-200 */\n"
"}\n"
"\n"
"/* ---------------------------\n"
"   Pequenos ajustes de container\n"
"   --------------------------- */\n"
"\n"
"/* Barra de status (se houver) */\n"
"QStatusBar {\n"
"  background: #312783;           /* cinza-50 */\n"
"  color: #f0f0f0;                /* cinza-700 */\n"
"  border-top: 1px solid #e5e7eb; /* cinza-200 */\n"
"  padding: 3px 6px;\n"
"}\n"
"\n"
"/* Barra de menu (QMenuBar) */\n"
"QMenuBar {\n"
"  background: #312783;\n"
"  color: #FFED00;\n"
"  border-bottom: 1px solid #e5e7eb;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"  padding: 4px 8px;\n"
"  background: transparent;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
" background: #2563fb;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QMenuBar::item:pressed  { \n"
"background: #2563fb;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"/* Menu popup (QMenu) */\n"
"QMenu {\n"
"  background: #312783;\n"
"  color: rgb(255, 255, 0);\n"
"  border: 1px solid #e5e7eb;\n"
"  padding: 4px "
                        "0;\n"
"}\n"
"\n"
"QMenu::item {\n"
"  padding: 6px 16px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"  background: #2563fb;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"  height: 1px;\n"
"  background: #e5e7eb;\n"
"  margin: 4px 6px;\n"
"}\n"
"\n"
"/* Redimensionamento  */\n"
"QSizeGrip {\n"
"  background: transparent;\n"
"  image: none;\n"
"  width: 0px;\n"
"  height: 0px;\n"
"  margin: 0;\n"
"  padding: 0;\n"
"}\n"
"\n"
"/* Fontes */\n"
"QPushButton,\n"
"QToolButton,\n"
"QTabBar::tab,\n"
"QMenuBar,\n"
"QMenu {\n"
"    font: 600 10pt \"Tahoma\";\n"
"}\n"
"\n"
"QLabel {\n"
"    font: 700 9pt \"Tahoma\";\n"
"}\n"
"\n"
"#texto{\n"
"background: #ffffff;\n"
"  color: #111827;\n"
"  border: 1px solid rgb(0,0,63);  \n"
"  border-radius: 6px;\n"
"  padding: 6px 8px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Email do Remetente", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Senha de App", None))
        self.buttonBox.setAccessibleIdentifier("")
    # retranslateUi

