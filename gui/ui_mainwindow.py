# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget bglh q o gustavo nao salvouqIsoQb.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(380, 360)
        MainWindow.setMinimumSize(QSize(380, 360))
        MainWindow.setMaximumSize(QSize(380, 360))
        MainWindow.setStyleSheet(u"/* Estilo simples e unificado para um app b\u00e1sico (MainWindow > QSS)\n"
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
"  border: 1px solid #d1d5db;     /* cinza-300 */\n"
"  border-radius: 6px;\n"
"  padding: 6px 12px;\n"
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
"/* Bot\u00e3o prim\u00e1rio */\n"
"QPushButton[class=\"primary\"] {\n"
"  background: #2563eb;           /* azul-600 */\n"
"  color: #ffffff;\n"
"  border-color: #1d4ed8;         /* azul-700 */\n"
"}\n"
"QPushButton[class=\"primary\"]:hover {\n"
"  background: #1e53c7;           /* hover */\n"
"  border-color: #1b47b1;\n"
"}\n"
"QPushButton[class=\"primary\"]:pressed {\n"
"  background: #1b47b1;           /* pressed */\n"
"}\n"
"QPushButton[class=\"primary\"]:disabled {\n"
"  background: #93c5fd;           /* az"
                        "ul-300 */\n"
"  color: #e5e7eb;\n"
"  border-color: #93c5fd;\n"
"}\n"
"\n"
"/* Bot\u00e3o secund\u00e1rio */\n"
"QPushButton[class=\"secondary\"] {\n"
"  background: #f3f4f6;           /* cinza-100 */\n"
"  color: #111827;\n"
"  border-color: #d1d5db;         /* cinza-300 */\n"
"}\n"
"QPushButton[class=\"secondary\"]:hover {\n"
"  background: #e5e7eb;           /* cinza-200 */\n"
"}\n"
"QPushButton[class=\"secondary\"]:pressed {\n"
"  background: #d1d5db;           /* cinza-300 */\n"
"}\n"
"\n"
"/* Bot\u00e3o de perigo (ex.: Excluir) */\n"
"QPushButton[class=\"danger\"] {\n"
"  background: #dc2626;           /* vermelho-600 */\n"
"  color: #ffffff;\n"
"  border-color: #b91c1c;         /* vermelho-700 */\n"
"}\n"
"QPushButton[class=\"danger\"]:hover {\n"
"  background: #b91c1c;\n"
"}\n"
"QPushButton[class=\"danger\"]:pressed {\n"
"  background: #991b1b;\n"
"}\n"
"\n"
"/* Bot\u00e3o \"text\" (sem preenchimento, estilo link) */\n"
"QPushButton[class=\"text\"] {\n"
"  background: transparent;\n"
"  color: #2563eb;"
                        "                /* azul-600 */\n"
"  border-color: transparent;\n"
"}\n"
"QPushButton[class=\"text\"]:hover {\n"
"  background: #eff6ff;           /* azul-50 */\n"
"}\n"
"QPushButton[class=\"text\"]:pressed {\n"
"  background: #dbeafe;           /* azul-100 */\n"
"}\n"
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
"  background: rgb(0, 0, 63);           /* cinza-50 */\n"
"  color: #f0f0f0;                /* cinza-700 */\n"
"  border-top: 1px solid #e5e7eb; /* cinza-200 */\n"
"  padding: 3px 6px;\n"
"}\n"
"\n"
"/* Barra de menu (QMenuBar) */\n"
"QMen"
                        "uBar {\n"
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
""
                        "/* Fontes */\n"
"QPushButton,\n"
"QToolButton,\n"
"QTabBar::tab,\n"
"QMenuBar,\n"
"QMenu {;\n"
"	font: 600 10pt \"Tahoma\";\n"
"}\n"
"\n"
"QLineEdit,\n"
"QComboBox,\n"
"QTextEdit,\n"
"QPlainTextEdit {\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 700 9pt \"Tahoma\";\n"
"}")
        self.actionEscrever_manualmente = QAction(MainWindow)
        self.actionEscrever_manualmente.setObjectName(u"actionEscrever_manualmente")
        self.action_csv = QAction(MainWindow)
        self.action_csv.setObjectName(u"action_csv")
        self.actionAdicionar_Remetente = QAction(MainWindow)
        self.actionAdicionar_Remetente.setObjectName(u"actionAdicionar_Remetente")
        self.actionAdicionar_um_Remetente = QAction(MainWindow)
        self.actionAdicionar_um_Remetente.setObjectName(u"actionAdicionar_um_Remetente")
        self.actionAdicionar_Destinat_rios = QAction(MainWindow)
        self.actionAdicionar_Destinat_rios.setObjectName(u"actionAdicionar_Destinat_rios")
        self.actionDestinatparios_Salvos = QAction(MainWindow)
        self.actionDestinatparios_Salvos.setObjectName(u"actionDestinatparios_Salvos")
        self.actionRemetente = QAction(MainWindow)
        self.actionRemetente.setObjectName(u"actionRemetente")
        self.actionDestinatario = QAction(MainWindow)
        self.actionDestinatario.setObjectName(u"actionDestinatario")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setToolTipDuration(-1)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 24pt \"Tahoma\";")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout_2.addWidget(self.widget)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy1)
        self.plainTextEdit.setMaximumSize(QSize(16777215, 110))

        self.verticalLayout_2.addWidget(self.plainTextEdit)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")

        self.horizontalLayout_2.addWidget(self.widget_4)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.horizontalLayout_2.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 380, 25))
        self.menuRemetente = QMenu(self.menubar)
        self.menuRemetente.setObjectName(u"menuRemetente")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuRemetente.menuAction())
        self.menuRemetente.addAction(self.actionRemetente)
        self.menuRemetente.addAction(self.actionDestinatario)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionEscrever_manualmente.setText(QCoreApplication.translate("MainWindow", u"Escrever manualmente", None))
        self.action_csv.setText(QCoreApplication.translate("MainWindow", u".csv", None))
        self.actionAdicionar_Remetente.setText(QCoreApplication.translate("MainWindow", u"Adicionar Remetente", None))
        self.actionAdicionar_um_Remetente.setText(QCoreApplication.translate("MainWindow", u"Adicionar um Remetente", None))
        self.actionAdicionar_Destinat_rios.setText(QCoreApplication.translate("MainWindow", u"Adicionar Destinat\u00e1rios", None))
        self.actionDestinatparios_Salvos.setText(QCoreApplication.translate("MainWindow", u"Destinat\u00e1rios Salvos", None))
        self.actionRemetente.setText(QCoreApplication.translate("MainWindow", u"Remetente", None))
        self.actionDestinatario.setText(QCoreApplication.translate("MainWindow", u"Destinat\u00e1rios", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enviador de Email", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Anexo", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.menuRemetente.setTitle(QCoreApplication.translate("MainWindow", u"Endere\u00e7os", None))
    # retranslateUi

