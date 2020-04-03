from PyQt5.QtWidgets import QWidget


class MenuWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle('Main Menu')
    
        self.show()
                
