# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget bglh q o gustavo nao salvouXoGEwA.ui'
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
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(380, 360)
        MainWindow.setMinimumSize(QSize(380, 360))
        MainWindow.setMaximumSize(QSize(380, 431))
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
"  color: #9ca3af;                /* ci"
                        "nza-400 */\n"
"  border-color: #e5e7eb;         /* cinza-200 */\n"
"}\n"
"\n"
"/* ---------------------------\n"
"   Pequenos ajustes de cont\u00eainer\n"
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
"  pad"
                        "ding: 4px 0;\n"
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
"QMenu {;\n"
"	font: 600 10pt \"Tahoma\";\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 700 9pt \"Tahoma\";\n"
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
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.texto = QWidget(self.widget_5)
        self.texto.setObjectName(u"texto")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.texto.sizePolicy().hasHeightForWidth())
        self.texto.setSizePolicy(sizePolicy2)
        self.texto.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.texto)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.textEdit = QTextEdit(self.texto)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)


        self.verticalLayout_4.addWidget(self.texto)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)
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

