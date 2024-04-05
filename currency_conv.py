# import re
import requests
from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QLineEdit
from PyQt5 import uic, QtWidgets
# import json


class Currency_converter(QtWidgets.QMainWindow):
    def __init__(self):
        super(Currency_converter, self).__init__()
        uic.loadUi("currency_conv.ui", self)
        self.show()
        # self.data = requests.get('url')
        # self.currencies = self.data['rates']
        self.clear_pushButton.clicked.connect(self.enter_amount_lineEdit.clear)
        self.clear_pushButton.clicked.connect(self.output_lineEdit.clear)
        self.close_pushButton.clicked.connect(exit)
        self.convert_pushButton.clicked.connect(self.convert_currency)

        response = requests.get('url')
        data = response.json()  # converted the data in json format first n then into dictionary
        # print(data)
        currencies = dict(data['rates']) 

        for values in data:
            self.from_comboBox.addItems(currencies.keys())
            self.to_comboBox.addItems(currencies.keys())

    #     response = requests.get('url')
    #     currency = response.json()

    def convert_currency(self):
        amount = float(self.enter_amount_lineEdit.text())
        # print(amount)
        converted_amount = amount * 83.29026
        print(converted_amount)
        self.output_lineEdit.setText(str(converted_amount))



if __name__ == "__main__":
    app = QApplication([])
    win = Currency_converter()
    app.exec()

