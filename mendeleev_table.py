import sys
import csv
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView, QMessageBox
from PyQt6.QtCore import Qt

class Mendeleev(QWidget):
    def Element(self, ryad, colvo):
        infa = self.tableWidget.item(ryad, colvo)
        element = infa.data(Qt.ItemDataRole.ToolTipRole)
        QMessageBox.information(self, "Информация об элементе", element)

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Нажмите на интересующий вас элемент периодической таблицы Д.И.Менделеева')
        self.setGeometry(100, 100, 2000, 1500)

        layout = QVBoxLayout()

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setRowCount(12)

        Rows =["1", "2", "3", "4", "5", "6", "7", "8"]
        Groups = ["1", "2", "3", "4.1", "4.2", "5.1", "5.2","6.1","6.2" ,"7","Лантаноиды","Актиноиды"]

        with open('Mendeleev.csv', newline='', encoding='utf-8') as cvsfile:
            ExceLFile = csv.reader(cvsfile)
            for ryad in ExceLFile:
                if len(ryad) >= 5:
                    ShortName = ryad[0]
                    FullName = ryad[1]
                    Group = ryad[2]
                    Period = ryad[3]
                    Mass = ryad[4]

                    item = QTableWidgetItem(ShortName)
                    item.setData(Qt.ItemDataRole.ToolTipRole, f"Полное название: {FullName}\nМасса: {Mass}")
                    self.tableWidget.setItem(int(Period) - 1, int(Group) - 1, item)

        self.tableWidget.setHorizontalHeaderLabels(Rows)
        self.tableWidget.setVerticalHeaderLabels(Groups)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.tableWidget.cellClicked.connect(self.Element)

app = QApplication(sys.argv)
tablitsa = Mendeleev()
tablitsa.show()
sys.exit(app.exec())
