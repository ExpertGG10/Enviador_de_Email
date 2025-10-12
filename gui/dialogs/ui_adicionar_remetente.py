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
"  background: rgb(0, 0, 127);\n"
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
"QLabel"
                        " {\n"
"  color: rgb(255, 255, 255); /* cinza-900 */\n"
"}\n"
"\n"
"/* T\u00edtulo e varia\u00e7\u00f5es */\n"
"QLabel[class=\"title\"] {\n"
"  font-size: 16pt;\n"
"  font-weight: 700;\n"
"}\n"
"QLabel[class=\"subtitle\"] {\n"
"  font-size: 12pt;\n"
"  font-weight: 600;\n"
"  color: #374151; /* cinza-700 */\n"
"}\n"
"\n"
"/* Texto auxiliar/menor */\n"
"QLabel[class=\"caption\"] {\n"
"  font-size: 9pt;\n"
"  color: #6b7280; /* cinza-500 */\n"
"}\n"
"\n"
"/* Texto suavizado */\n"
"QLabel[class=\"muted\"] {\n"
"  color: #6b7280; /* cinza-500 */\n"
"}\n"
"\n"
"/* ---------------------------\n"
"   Inputs (QLineEdit, QTextEdit, QPlainTextEdit)\n"
"   --------------------------- */\n"
"QLineEdit,\n"
"QTextEdit,\n"
"QPlainTextEdit {\n"
"  background: rgb(255, 255, 255);\n"
"  color: #111827;\n"
"  border: 1px solid #d1d5db;    /* cinza-300 */\n"
"  border-radius: 6px;\n"
"  padding: 6px 8px;\n"
"}\n"
"\n"
"QLineEdit:focus,\n"
"QTextEdit:focus,\n"
"QPlainTextEdit:focus {\n"
"  border: 1px solid #2563eb;    /* foco azul"
                        " */\n"
"  background: #ffffff;\n"
"}\n"
"\n"
"/* Desabilitado */\n"
"QLineEdit:disabled,\n"
"QTextEdit:disabled,\n"
"QPlainTextEdit:disabled {\n"
"  color: #9ca3af;\n"
"  background: #f3f4f6;          /* cinza-100 */\n"
"  border-color: #e5e7eb;         /* cinza-200 */\n"
"}\n"
"\n"
"/* Estados via \"class\" */\n"
"QLineEdit[class=\"error\"],\n"
"QTextEdit[class=\"error\"],\n"
"QPlainTextEdit[class=\"error\"] {\n"
"  border-color: #dc2626;         /* vermelho-600 */\n"
"  background: #fef2f2;           /* vermelho-50 */\n"
"  color: #7f1d1d;\n"
"}\n"
"\n"
"QLineEdit[class=\"success\"],\n"
"QTextEdit[class=\"success\"],\n"
"QPlainTextEdit[class=\"success\"] {\n"
"  border-color: #16a34a;         /* verde-600 */\n"
"  background: #f0fdf4;           /* verde-50 */\n"
"  color: #14532d;\n"
"}\n"
"\n"
"/* ---------------------------\n"
"   Bot\u00f5es (QPushButton)\n"
"   --------------------------- */\n"
"QPushButton {\n"
"  background: #e5e7eb;           /* cinza-200 */\n"
"  color: #111827;                /* cin"
                        "za-900 */\n"
"  font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #dbe1e6;           /* leve escurecido */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #cfd6dc;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"  background: #f3f4f6;           /* cinza-100 */\n"
"  color: #9ca3af;                /* cinza-400 */\n"
"  border-color: #e5e7eb;         /* cinza-200 */\n"
"}\n"
"\n"
"/* Bot\u00e3o \"text\" (sem preenchimento, estilo link) */\n"
"\n"
"\n"
"\n"
"\n"
"/* ---------------------------\n"
"   Pequenos ajustes de cont\u00eainer\n"
"   --------------------------- */\n"
"\n"
"/* QGroupBox simples */\n"
"QGroupBox {\n"
"  border: 1px solid #e5e7eb;     /* cinza-200 */\n"
"  border-radius: 8px;\n"
"  margin-top: 12px;\n"
"}\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  left: 8px;\n"
"  padding: 0 4px;\n"
"  color: #374151;                /* cinza-700 */\n"
"  font-weight: 600;\n"
"}\n"
"\n"
"/* Barra de status (se houver) */\n"
"QStatusBar {\n"
"  background: rgb(0, 0, 63)"
                        ";           /* cinza-50 */\n"
"  color: #f0f0f0;                /* cinza-700 */\n"
"  border-top: 1px solid #e5e7eb; /* cinza-200 */\n"
"  padding: 3px 6px;\n"
"}\n"
"\n"
"/* Barra de menu (QMenuBar) */\n"
"QMenuBar {\n"
"  background: rgb(0, 0, 63);\n"
"  color: #ffff00;\n"
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
" background: #2563eb;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QMenuBar::item:pressed  { \n"
"background: #2563eb;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"/* Menu popup (QMenu) */\n"
"QMenu {\n"
"  background: rgb(0, 0, 63);\n"
"  color: rgb(255, 255, 0);\n"
"  border: 1px solid #e5e7eb;\n"
"  padding: 4px 0;\n"
"}\n"
"\n"
"QMenu::item {\n"
"  padding: 6px 16px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"  background: #2563eb;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"  height: 1px;\n"
"  background: #e5e7eb;\n"
""
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
"QMenu {;\n"
"	font: 600 10pt \"Tahoma\";\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 700 9pt \"Tahoma\";\n"
"}")
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

