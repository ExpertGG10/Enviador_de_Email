import sys
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    
    # Configurar aplicação
    app.setApplicationName("Email Sender")
    app.setApplicationVersion("1.0")
    app.setOrganizationName("Rio Software")
    
    # Criar e mostrar janela principal
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()