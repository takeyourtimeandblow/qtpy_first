import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)


# Унаследуем наш класс от простейшего графического примитива QWidget
class WordSwapper(QWidget):

    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # В метод initUI() будем выносить всю настройку интерфейса,
        # чтобы не перегружать инициализатор
        
        self.arrow = '⬇️'
        self.initUI()

    def initUI(self):
        # (?, ?, x, y)
        self.setGeometry(0, 0, 500, 0)
        # А также его заголовок
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
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex = WordSwapper()
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())
