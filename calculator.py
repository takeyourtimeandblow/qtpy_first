import sys
from PyQt5.QtWidgets import (
	QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QCheckBox,
    QSpinBox,
    QLabel,
    QPushButton,
    QLineEdit   
)

ops = '+-*/'

digits_and_dot = (
    '789',
    '456',
    '123',
    '0.'
)

class CalculatorMain(QWidget):
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
	def initUI(self):
	    self.setWindowTitle('Калькулятор')
	    
	    v_layout = QVBoxLayout(self)
	    self.history = [
	        QLabel(),
	        QLabel(),
	        QLabel('0')
	    ]
	    self.label_num = 1
	    k_lyt = QGridLayout()
	    
	    for i, l in enumerate(ops):
	        button = QPushButton(l)
	        button.clicked.connect(self.next)
	        k_lyt.addWidget(button, 0, i)
	    for i, l in enumerate(digits_and_dot):
		    for j, b in enumerate(l):
		        button = QPushButton(b)
		        button.clicked.connect(self.tap)
		        k_lyt.addWidget(button, i+1, j)
	    cl_b = QPushButton('cl')
	    cl_b.clicked.connect(self.clear)
	    k_lyt.addWidget(cl_b, 0, len(ops))
	    
	    calc_res = QPushButton('=')
	    calc_res.clicked.connect(self.calculate)
	    
	    self.message = QLabel()
	    
	    for w in self.history:
	        v_layout.addWidget(w)    
	    
	    v_layout.addLayout(k_lyt)
	    v_layout.addWidget(calc_res)
	    v_layout.addWidget(self.message)
	    
	def next(self):
	    try:
	        if self.history[0].text():
	            self.history[0].setText(str(eval(f'{self.history[0].text()}{self.history[1].text()}{self.history[2].text()}')))
	        else:
	            self.history[0].setText(self.history[2].text())
	        self.history[1].setText(self.sender().text())
	        self.history[2].setText('0')
	        
	        self.message.setText(' ')
	    except ZeroDivisionError:
	        self.message.setText('Деление На ноль')

	    
	def tap(self):
	    sended = self.sender().text()
	    if self.history[2].text()[0] == '0' and len(self.history[2].text()) < 2 and (sended != '.' and self.history[2].text()[-1] != '.'):
	        self.history[2].setText(f'{self.history[2].text()[1:]}')    
	    self.history[2].setText(f'{self.history[2].text()}{sended}')
	    
	def clear(self):
	    self.history[2].setText('0')
	    self.history[0].setText('')
	    self.history[1].setText('')
	    
	def calculate(self):
	    try:
	        self.history[2].setText(str(eval(f'{self.history[0].text()}{self.history[1].text()}{self.history[2].text()}')))
	        self.history[0].setText('')
	        self.history[1].setText('')
	        
	        self.message.setText(' ')
	    except ZeroDivisionError:
	        self.message.setText('Деление На ноль')
		
		
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalculatorMain()
    ex.show()
    sys.exit(app.exec())   
    
		
