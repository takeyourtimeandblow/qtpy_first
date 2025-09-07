import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton
)


# Унаследуем наш класс от простейшего графического примитива QWidget
class Calculator(QWidget):
    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # В метод initUI() будем выносить всю настройку интерфейса,
        # чтобы не перегружать инициализатор
        self.initUI()

    def initUI(self):
        # Зададим размер и положение нашего виджета,
        self.setGeometry(0, 0, 500, 0)
        # А также его заголовок
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
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex = Calculator()
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())
