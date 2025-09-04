import sys


from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton
)



class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 500, 0)
        self.setWindowTitle('Калькулятор (своеобразный)')
        
        layout = QVBoxLayout(self)
        
        self.line1 = QLineEdit(self)
        self.line2 = QLineEdit(self)
        
        
        btn = QPushButton('Вычислить')
        btn.clicked.connect(self.evalAndPrint)
        
        layout.addWidget(self.line1)
        layout.addWidget(btn)
        layout.addWidget(self.line2)
        
    def evalAndPrint(self):
        try:
            self.line2.setText(f'{self.line1.text()} -> {str(eval(self.line1.text()))}')
        except Exception as e:
            self.line2.setText(f'Error: {e}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
