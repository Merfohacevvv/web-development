import data.icons
from find_route import alg
from display import draw_result
import math
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    S_matrix = []
    def setupUi(self, MainWindow: QtWidgets.QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 812)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1081, 791))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(68, 56, 72);\n"
"    border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticesList = QtWidgets.QListWidget(self.frame)
        self.verticesList.setEnabled(True)
        self.verticesList.setGeometry(QtCore.QRect(715, 30, 331, 221))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.verticesList.setFont(font)
        self.verticesList.setAcceptDrops(False)
        self.verticesList.setStyleSheet("QListWidget {\n"
"    background-color: rgb(124, 113, 116);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    padding: 10px;\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QListView::item\n"
"{\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QListView::item:selected\n"
"{\n"
"    border: 3px 3px solid white;\n"
"    background-color: rgb(116, 108, 106);\n"
"}")
        self.verticesList.setObjectName("verticesList")
        self.edgesList = QtWidgets.QListWidget(self.frame)
        self.edgesList.setEnabled(True)
        self.edgesList.setGeometry(QtCore.QRect(715, 310, 331, 431))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.edgesList.setFont(font)
        self.edgesList.setAcceptDrops(False)
        self.edgesList.setStyleSheet("QListWidget {\n"
"    background-color: rgb(124, 113, 116);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    padding: 10px;\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QListView::item\n"
"{\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QListView::item:selected\n"
"{\n"
"    border: 3px 3px solid white;\n"
"    background-color: rgb(116, 108, 106);\n"
"}")
        self.edgesList.setObjectName("edgesList")
        self.startProgramm = QtWidgets.QPushButton(self.frame)
        self.startProgramm.clicked.connect(self.start_programm)
        self.startProgramm.setGeometry(QtCore.QRect(200, 720, 250, 40))
        self.startProgramm.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255,255,255, 0.88);\n"
"    border-radius: 20px;\n"
"    font: 12pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255,255,255, 0.7);\n"
"}")
        self.startProgramm.setObjectName("startProgramm")
        self.verticesLabel = QtWidgets.QLabel(self.frame)
        self.verticesLabel.setGeometry(QtCore.QRect(30, 20, 241, 31))
        self.verticesLabel.setStyleSheet("QLabel {\n"
"    color: rgba(255,255,255,0.88);\n"
"    font: 16pt \"Roboto\";\n"
"}")
        self.verticesLabel.setObjectName("verticesLabel")
        self.edgeLabel = QtWidgets.QLabel(self.frame)
        self.edgeLabel.setGeometry(QtCore.QRect(30, 300, 271, 31))
        self.edgeLabel.setStyleSheet("QLabel {\n"
"    color: rgba(255,255,255,0.88);\n"
"    font: 16pt \"Roboto\";\n"
"}")
        self.edgeLabel.setObjectName("edgeLabel")
        self.addCityNameLabel = QtWidgets.QLabel(self.frame)
        self.addCityNameLabel.setGeometry(QtCore.QRect(40, 90, 241, 31))
        self.addCityNameLabel.setStyleSheet("QLabel {\n"
"    color: rgba(255,255,255,0.88);\n"
"    font: 16pt \"Roboto\";\n"
"}")
        self.addCityNameLabel.setObjectName("addCityNameLabel")
        self.addCityName = QtWidgets.QLineEdit(self.frame)
        self.addCityName.setGeometry(QtCore.QRect(204, 90, 320, 31))
        self.addCityName.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(124, 113, 116);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font: 10pt \"Roboto\";\n"
"    color: white;\n"
"    padding: 0 10px;\n"
"}")
        self.addCityName.setText("")
        self.addCityName.setObjectName("addCityName")
        self.addCityButton = QtWidgets.QPushButton(self.frame)
        self.addCityButton.clicked.connect(self.add_city)
        self.addCityButton.setGeometry(QtCore.QRect(60, 175, 181, 40))
        self.addCityButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255,255,255, 0.88);\n"
"    border-radius: 20px;\n"
"    font: 12pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255,255,255, 0.7);\n"
"}")
        self.addCityButton.setCheckable(False)
        self.addCityButton.setChecked(False)
        self.addCityButton.setAutoDefault(False)
        self.addCityButton.setDefault(False)
        self.addCityButton.setObjectName("addCityButton")
        self.delCityButton = QtWidgets.QPushButton(self.frame)
        self.delCityButton.clicked.connect(self.delete_city)
        self.delCityButton.setGeometry(QtCore.QRect(330, 175, 181, 40))
        self.delCityButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255,255,255, 0.88);\n"
"    border-radius: 20px;\n"
"    font: 12pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255,255,255, 0.7);\n"
"}")
        self.delCityButton.setObjectName("delCityButton")
        self.fromEdge = QtWidgets.QComboBox(self.frame)
        self.fromEdge.setGeometry(QtCore.QRect(40, 390, 211, 22))
        self.fromEdge.setStyleSheet("QComboBox {\n"
"    background-color: rgb(124, 113, 116);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font: 10pt \"Roboto\";\n"
"    color: white;\n"
"    padding: 0 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"    image: url(:/icons/352021_arrow_drop down_icon.ico);\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"\n"
"QComboBox QListView{\n"
"    background-color: #4f4f4f;\n"
"    color: white;\n"
"    selection-background-color: #999999;\n"
"    selection-color: #4f4f4f;\n"
"    border-radius: none;\n"
"}")
        self.fromEdge.setObjectName("fromEdge")
        self.fromEdgeLabel = QtWidgets.QLabel(self.frame)
        self.fromEdgeLabel.setGeometry(QtCore.QRect(40, 345, 101, 31))
        self.fromEdgeLabel.setStyleSheet("QLabel {\n"
"    color: rgba(255,255,255,0.88);\n"
"    font: 16pt \"Roboto\";\n"
"}")
        self.fromEdgeLabel.setObjectName("fromEdgeLabel")
        self.toEdgeLabel = QtWidgets.QLabel(self.frame)
        self.toEdgeLabel.setGeometry(QtCore.QRect(315, 345, 71, 31))
        self.toEdgeLabel.setStyleSheet("QLabel {\n"
"    color: rgba(255,255,255,0.88);\n"
"    font: 16pt \"Roboto\";\n"
"}")
        self.toEdgeLabel.setObjectName("toEdgeLabel")
        self.toEdge = QtWidgets.QComboBox(self.frame)
        self.toEdge.setGeometry(QtCore.QRect(315, 390, 211, 22))
        self.toEdge.setStyleSheet("QComboBox {\n"
"    background-color: rgb(124, 113, 116);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font: 10pt \"Roboto\";\n"
"    color: white;\n"
"    padding: 0 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"    image: url(:/icons/352021_arrow_drop down_icon.ico);\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"\n"
"QComboBox QListView{\n"
"    background-color: #4f4f4f;\n"
"    color: white;\n"
"    selection-background-color: #999999;\n"
"    selection-color: #4f4f4f;\n"
"    border-radius: none;\n"
"}")
        self.toEdge.setObjectName("toEdge")
        self.lengthEdgeLabel = QtWidgets.QLabel(self.frame)
        self.lengthEdgeLabel.setGeometry(QtCore.QRect(553, 345, 91, 31))
        self.lengthEdgeLabel.setStyleSheet("QLabel {\n"
"    color: rgba(255,255,255,0.88);\n"
"    font: 16pt \"Roboto\";\n"
"}")
        self.lengthEdgeLabel.setObjectName("lengthEdgeLabel")
        self.lengthEdge = QtWidgets.QSpinBox(self.frame)
        self.lengthEdge.setGeometry(QtCore.QRect(553, 390, 91, 22))
        self.lengthEdge.setStyleSheet("QSpinBox {\n"
"    background-color: rgb(124, 113, 116);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font: 10pt \"Roboto\";\n"
"    color: white;\n"
"    padding: 0 10px;\n"
"}")
        self.lengthEdge.setMinimum(1)
        self.lengthEdge.setMaximum(999999999)
        self.lengthEdge.setObjectName("lengthEdge")
        self.addEdgeButton = QtWidgets.QPushButton(self.frame)
        self.addEdgeButton.clicked.connect(self.add_edge)
        self.addEdgeButton.setGeometry(QtCore.QRect(60, 480, 181, 40))
        self.addEdgeButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255,255,255, 0.88);\n"
"    border-radius: 20px;\n"
"    font: 12pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255,255,255, 0.7);\n"
"}")
        self.addEdgeButton.setObjectName("addEdgeButton")
        self.deleteEdgeButton = QtWidgets.QPushButton(self.frame)
        self.deleteEdgeButton.clicked.connect(self.delete_edge)
        self.deleteEdgeButton.setGeometry(QtCore.QRect(330, 480, 181, 40))
        self.deleteEdgeButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255,255,255, 0.88);\n"
"    border-radius: 20px;\n"
"    font: 12pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255,255,255, 0.7);\n"
"}")
        self.deleteEdgeButton.setObjectName("deleteEdgeButton")
        self.findLabel = QtWidgets.QLabel(self.frame)
        self.findLabel.setGeometry(QtCore.QRect(30, 545, 201, 31))
        self.findLabel.setStyleSheet("QLabel {\n"
"    color: rgba(255,255,255,0.88);\n"
"    font: 16pt \"Roboto\";\n"
"}")
        self.findLabel.setObjectName("findLabel")
        self.toFindLabel = QtWidgets.QLabel(self.frame)
        self.toFindLabel.setGeometry(QtCore.QRect(400, 590, 71, 31))
        self.toFindLabel.setStyleSheet("QLabel {\n"
"    color: rgba(255,255,255,0.88);\n"
"    font: 16pt \"Roboto\";\n"
"}")
        self.toFindLabel.setObjectName("toFindLabel")
        self.toFind = QtWidgets.QComboBox(self.frame)
        self.toFind.setGeometry(QtCore.QRect(400, 635, 250, 22))
        self.toFind.setStyleSheet("QComboBox {\n"
"    background-color: rgb(124, 113, 116);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font: 10pt \"Roboto\";\n"
"    color: white;\n"
"    padding: 0 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"    image: url(:/icons/352021_arrow_drop down_icon.ico);\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"\n"
"QComboBox QListView{\n"
"    background-color: #4f4f4f;\n"
"    color: white;\n"
"    selection-background-color: #999999;\n"
"    selection-color: #4f4f4f;\n"
"    border-radius: none;\n"
"}")
        self.toFind.setObjectName("toFind")
        self.fromFind = QtWidgets.QComboBox(self.frame)
        self.fromFind.setGeometry(QtCore.QRect(40, 635, 250, 22))
        self.fromFind.setStyleSheet("QComboBox {\n"
"    background-color: rgb(124, 113, 116);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font: 10pt \"Roboto\";\n"
"    color: white;\n"
"    padding: 0 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"    image: url(:/icons/352021_arrow_drop down_icon.ico);\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"\n"
"QComboBox QListView{\n"
"    background-color: #4f4f4f;\n"
"    color: white;\n"
"    selection-background-color: #999999;\n"
"    selection-color: #4f4f4f;\n"
"    border-radius: none;\n"
"}")
        self.fromFind.setObjectName("fromFind")
        self.fromFindLabel = QtWidgets.QLabel(self.frame)
        self.fromFindLabel.setGeometry(QtCore.QRect(40, 590, 101, 31))
        self.fromFindLabel.setStyleSheet("QLabel {\n"
"    color: rgba(255,255,255,0.88);\n"
"    font: 16pt \"Roboto\";\n"
"}")
        self.fromFindLabel.setObjectName("fromFindLabel")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.clicked.connect(lambda : MainWindow.close())
        self.closeButton.setGeometry(QtCore.QRect(1065, -12, 50, 50))
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setStyleSheet("QPushButton {\n"
"    background-color: none;\n"
"    border: none;\n"
"    font: 87 24pt \"Arial Black\";\n"
"    color: rgb(255, 0, 127);\n"
"    border-radius: 50px;\n"
"}")
        self.closeButton.setObjectName("closeButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startProgramm.setText(_translate("MainWindow", "Запустить программу"))
        self.verticesLabel.setText(_translate("MainWindow", "Добавить города"))
        self.edgeLabel.setText(_translate("MainWindow", "Добавить маршруты"))
        self.addCityNameLabel.setText(_translate("MainWindow", "Название :"))
        self.addCityButton.setText(_translate("MainWindow", "Добавить"))
        self.delCityButton.setText(_translate("MainWindow", "Удалить"))
        self.fromEdgeLabel.setText(_translate("MainWindow", "Откуда:"))
        self.toEdgeLabel.setText(_translate("MainWindow", "Куда:"))
        self.lengthEdgeLabel.setText(_translate("MainWindow", "Длина:"))
        self.addEdgeButton.setText(_translate("MainWindow", "Добавить"))
        self.deleteEdgeButton.setText(_translate("MainWindow", "Удалить"))
        self.findLabel.setText(_translate("MainWindow", "Найти маршрут"))
        self.toFindLabel.setText(_translate("MainWindow", "Куда:"))
        self.fromFindLabel.setText(_translate("MainWindow", "Откуда:"))
        self.closeButton.setText(_translate("MainWindow", "X"))

    def add_city(self):
        if (self.addCityName.text().strip() == ""):
            QtWidgets.QMessageBox.critical(MainWindow, "Ошибка", "Вы не можете добавить город без названия")
            return
        elif (len(self.verticesList.findItems(self.addCityName.text().strip(), QtCore.Qt.MatchExactly)) != 0):
            QtWidgets.QMessageBox.critical(MainWindow, "Ошибка", "Город с таким названием уже есть")
            return
        for list in [self.verticesList, self.fromEdge, self.toEdge, self.fromFind, self.toFind]:
            list.addItem(self.addCityName.text().strip())
        self.addCityName.setText("")
        for vertix in self.S_matrix:
            vertix.append(0)
        self.S_matrix.append([0]*(len(self.S_matrix)+1))

    def delete_city(self):
        if (len(self.verticesList.selectedItems()) == 0):
            QtWidgets.QMessageBox.critical(MainWindow, "Ошибка", "Выберите элемент который ходите удалить")
            return
        self.S_matrix.pop(self.verticesList.selectedIndexes()[0].row())
        for vertix in self.S_matrix:
                vertix.pop(self.verticesList.selectedIndexes()[0].row())
        for list in [self.fromEdge, self.toEdge, self.fromFind, self.toFind]:
            list.removeItem(self.verticesList.selectedIndexes()[0].row())
        edge = 0
        while (edge < self.edgesList.count()):
            if (self.verticesList.selectedItems()[0].text().strip() in self.edgesList.item(edge).text()):
                self.edgesList.takeItem(edge)
            else:
                edge += 1
        self.verticesList.takeItem(self.verticesList.selectedIndexes()[0].row())

    def add_edge(self):
        if (self.fromEdge.currentText() == "" or self.toEdge.currentText() == ""):
            QtWidgets.QMessageBox.critical(MainWindow, "Ошибка", "Выберите города")
            return
        elif (self.fromEdge.currentText() == self.toEdge.currentText()):
            QtWidgets.QMessageBox.critical(MainWindow, "Ошибка", "Города должны быть различны")
            return
        if (self.S_matrix[self.fromEdge.currentIndex()][self.toEdge.currentIndex()] != 0):
            self.edgesList.findItems(f"{self.fromEdge.currentText()} | {self.toEdge.currentText()} |", QtCore.Qt.MatchContains)[0].setText(f"{self.fromEdge.currentText()} | {self.toEdge.currentText()} | {self.lengthEdge.text()}")
        else:
            self.edgesList.addItem(f"{self.fromEdge.currentText()} | {self.toEdge.currentText()} | {self.lengthEdge.text()}")
        self.S_matrix[self.fromEdge.currentIndex()][self.toEdge.currentIndex()] = int(self.lengthEdge.text())

    def delete_edge(self):
        if (len(self.edgesList.selectedItems()) == 0):
            QtWidgets.QMessageBox.critical(MainWindow, "Ошибка", "Выберите маршрут который ходите удалить")
            return
        path = self.edgesList.selectedItems()[0].text().split(" | ")
        self.edgesList.takeItem(self.edgesList.selectedIndexes()[0].row())
        from_city = self.verticesList.indexFromItem(self.verticesList.findItems(path[0], QtCore.Qt.MatchExactly)[0]).row()
        to_city = self.verticesList.indexFromItem(self.verticesList.findItems(path[1], QtCore.Qt.MatchExactly)[0]).row()
        self.S_matrix[from_city][to_city] = 0

    def convert_matrix(self):
        converted_matrix = []
        for i in range(len(self.S_matrix)):
            converted_matrix.append(self.S_matrix[i].copy())
        for i in range(len(converted_matrix)):
            for j in range(len(converted_matrix)):
                if (i != j and converted_matrix[i][j] == 0):
                    converted_matrix[i][j] = math.inf
        return converted_matrix

    def start_programm(self):
        if (self.fromFind.currentText() == "" or self.fromFind.currentText() == ""):
            QtWidgets.QMessageBox.critical(MainWindow, "Ошибка", "Выберите откуда и куда вы ходите проложить маршрут")
            return
        elif (self.fromFind.currentText() == self.toFind.currentText()):
            QtWidgets.QMessageBox.information(MainWindow, "Победа", "Вы пришли")
            return
        result = alg(self.convert_matrix(), self.fromFind.currentIndex(), self.toFind.currentIndex())
        if (result is None or math.isinf(result['len_route'])):
            QtWidgets.QMessageBox.critical(MainWindow, "Проигрыш", "К сожалению невозможно создать такой маршруты")
            return
        QtWidgets.QMessageBox.information(MainWindow, "Победа", f"Длина маршрута: {result['len_route']}")
        draw_result(self.S_matrix, [self.verticesList.item(i).text() for i in range(self.verticesList.count())], result['route'])

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app_icon = QtGui.QIcon()
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
