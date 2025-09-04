import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)


class WordSwapper(QWidget):

    def __init__(self):
        super().__init__()
        
        self.arrow = '⬇️'
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 500, 0)
        self.setWindowTitle('Перекидыватель Слов')
        
        layout = QVBoxLayout(self)
        
        label1 = QLabel('Верхнее поле')
        self.edit_line1 = QLineEdit('')
        
        self.button = QPushButton(self.arrow)
        self.button.clicked.connect(self.swap)
        
        label2 = QLabel('Нижнее поле')
        self.edit_line2 = QLineEdit('') 
        
        
        layout.addWidget(label1)
        layout.addWidget(self.edit_line1)
        layout.addWidget(self.button)
        layout.addWidget(label2)
        layout.addWidget(self.edit_line2)
        
    def swap(self):
        if self.arrow == '⬇️':
            self.edit_line2.setText(self.edit_line1.text())
            self.edit_line1.setText('')
            self.arrow = '⬆️'
        else: 
            self.edit_line1.setText(self.edit_line2.text())
            self.edit_line2.setText('')
            self.arrow = '⬇️'
            
        self.button.setText(self.arrow)
            
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordSwapper()
    ex.show()
    sys.exit(app.exec())
