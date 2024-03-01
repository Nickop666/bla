import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coffee App")
        self.setGeometry(100, 100, 600, 400)

        self.db = sqlite3.connect("coffee.sqlite")
        self.cursor = self.db.cursor()

        self.create_table_view()
        self.show()

    def create_table_view(self):
        self.table_view = QtWidgets.QTableView()
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["ID", "Name", "Roast Level", "Ground/Whole Bean", "Flavor Description", "Price", "Volume"])
        self.table_view.setModel(self.model)
        self.table_view.resizeColumnsToContents()

        self.cursor.execute("SELECT * FROM coffee")
        for row in self.cursor.fetchall():
            self.model.appendRow([QtWidgets.QStandardItem(str(row[0])),
                                 QtWidgets.QStandardItem(row[1]),
                                 QtWidgets.QStandardItem(row[2]),
                                 QtWidgets.QStandardItem(row[3]),
                                 QtWidgets.QStandardItem(row[4]),
                                 QtWidgets.QStandardItem(str(row[5])),
                                 QtWidgets.QStandardItem(str(row[6]))])

        self.setCentralWidget(self.table_view)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    coffee_app = CoffeeApp()
    sys.exit(app.exec_())
