import sys
from PyQt5.QtWidgets import (
	QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QCheckBox,
    QSpinBox,
    QLabel,
    QPushButton
)

food = {
    'Борщ': 100,
    'Драники': 120,
    'Картофельное пюре': 40,
    'Салат "Цезарь"': 100,
    'Морс': 30,
    'Филе курицы': 100,
    'Сосиска в тесте': 60,
    'Чёрный чай': 20,
}


class Order(QWidget):
	def __init__(self):
		super().__init__()
		
		self.w = None
		self.spinboxes = {}
		self.initUI()
	
	def initUI(self):
	    self.setGeometry(0, 0, 500, 500)
	    self.setWindowTitle('Меню')
	    v_layout = QVBoxLayout(self)
	    order_layout = QGridLayout()
	    
	    for i, (f, p) in enumerate(food.items()):
	        checkb = QCheckBox(f)
	        checkb.clicked.connect(self.include)
	        self.spinboxes[f] = QSpinBox()
	        self.spinboxes[f].setRange(1, 15)
	        self.spinboxes[f].setEnabled(False)
	        
	        order_layout.addWidget(checkb, i, 0)
	        order_layout.addWidget(QLabel(str(p) + ' руб.'), i, 1)
	        order_layout.addWidget(self.spinboxes[f], i, 2)
	    
	    button = QPushButton('Напечатать Чек')
	    button.clicked.connect(self.proceed)
	    
	    v_layout.addLayout(order_layout)
	    v_layout.addWidget(button)
	        
	def include(self):
	    self.spinboxes[self.sender().text()].setEnabled(self.sender().isChecked())
	    
	def proceed(self):
	    s = {x: y*self.spinboxes[x].value() for x, y in food.items() if self.spinboxes[x].isEnabled()}
	    if self.w is None:
	        self.w = OrderCheck(s)
	        self.w.show()
	    else:
	        self.w = None
	        self.proceed()
	    
	    
class OrderCheck(QWidget):
    def __init__(self, s):
        super().__init__()
        
        self.order = s
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Чек')
        layout = QVBoxLayout(self)
        for x, y in self.order.items():
            layout.addWidget(QLabel(f'{x}{"."*(50-len(x)-len(str(y)))}{y} р.'))
        layout.addWidget(QLabel(f'===============\nИТОГО: {sum(self.order.values())} руб.'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Order()
    ex.show()
    sys.exit(app.exec())   
