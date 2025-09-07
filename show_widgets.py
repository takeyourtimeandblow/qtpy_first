import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QDial,
    QDoubleSpinBox,
    QLCDNumber,
    QCheckBox
)


class ShowWidgets(QWidget):

    def __init__(self):
        super().__init__()
        
        self.arrow = '⬇️'
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 300, 0)
        self.setWindowTitle('Выключатель Виджетов')
        
        self.layout = QGridLayout(self)
        
        widgets = [
            QDial,
            QDoubleSpinBox,
            QLCDNumber
        ]
        self.checks = []
        for i in range(len(widgets)):
            self.checks.append(QCheckBox())
            self.layout.addWidget(self.checks[i], i, 1)
            self.checks[i].clicked.connect(self.changedState)
            
            self.layout.addWidget(widgets[i](), i, 2)
            
        
        
    def changedState(self):
        for i in range(self.layout.rowCount()):
            if self.checks[i].isChecked():
                self.layout.itemAtPosition(i, 2).widget().hide()
            else: self.layout.itemAtPosition(i, 2).widget().show()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowWidgets()
    ex.show()
    sys.exit(app.exec())
