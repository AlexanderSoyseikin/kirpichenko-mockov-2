import sys
import sqlite3
from Эспрессо_pyy import Ui_MainWindow
from Капучино_addEditCoffeeForm import Ui_MainWindow_2
from PyQt5 import QtWidgets


def main():
    class MyWidget_2(QtWidgets.QMainWindow, Ui_MainWindow_2):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.comboBox.setVisible(False)
            self.textEdit.setVisible(False)
            self.textEdit_2.setVisible(False)
            self.pushButton_5.setVisible(False)
            self.pushButton_5.setVisible(False)
            self.pushButton_3.clicked.connect(self.exit)
            self.pushButton_2.clicked.connect(self.add)

        def add(self):
            self.textEdit.setVisible(True)


        def exit(self):
            self.w = MyWidget()
            self.w.show()
            self.close()

    class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.pushButton.clicked.connect(self.cofi)
            self.conf = 0

        def cofi(self):
            self.conf += 1
            if self.conf == 2:
                self.w = MyWidget_2()
                self.w.show()
                self.close()
            con = sqlite3.connect("Эспрессо_coffee.db")
            cur = con.cursor()
            result = cur.execute("""SELECT * FROM coffee""").fetchall()
            con.close()
            self.tableWidget.setColumnCount(7)
            self.tableWidget.setRowCount(len(result))
            for i in range(len(result)):
                for j in range(len(result[i])):
                    self.tableWidget.setItem(int(i), int(j), QtWidgets.QTableWidgetItem(result[i][j]))

    if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        ex = MyWidget()
        ex.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()

