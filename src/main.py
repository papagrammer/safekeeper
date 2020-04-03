import sys
from ui import MenuWidget
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = MenuWidget()
    
    sys.exit(app.exec_())