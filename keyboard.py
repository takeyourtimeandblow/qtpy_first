import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton
)

qwerty = (
    {
        'q': '--.-',
        'w': '.--',
        'e': '.',
        'r': '.-.',
        't': '-',
        'y': '-.--',
        'u': '..-',
        'i': '..',
        'o': '---',
        'p': '.--.',
    },
    {
        'a': '.-',
        's': '...',
        'd': '-..',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
    },
    {
        'z': '--..',
        'x': '-..-',
        'c': '-.-.',
        'v': '...-',
        'b': '-...',
        'n': '-.',
        'm': '--',
    }
)

class KeyBoard(QWidget):
    def __init__(self):
        super().__init__()
    
        self.initUI()
    
    def initUI(self):
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle('Виртуальная Клавиатура QWERTY Морзе')
        layout = QVBoxLayout(self)
        
        self.edit_line = QLineEdit('')
        
        layout.addWidget(self.edit_line)
        
        grid_layout = QGridLayout()
        
        
        for n, line in enumerate(qwerty):
            for n1, i in enumerate(line.keys()):
                grid_layout.addWidget(QPushButton(i), n, n1)
                grid_layout.itemAtPosition(n, n1).widget().clicked.connect(self.tap)
                
        layout.addLayout(grid_layout)
    
    def tap(self):
        for d in range(len(qwerty)):
            if self.sender().text() in qwerty[d].keys():
                index = d
                break
            else:
                continue
            self.edit_line.setText(f'{self.edit_line.text()}x')
            break
        self.edit_line.setText(f'{self.edit_line.text()}{qwerty[index][self.sender().text()]}')
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = KeyBoard()
    ex.show()
    sys.exit(app.exec())    


