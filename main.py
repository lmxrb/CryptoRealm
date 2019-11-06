import apirequest
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import PyQt5.QtGui


#filedict = apirequest.updateDB(apirequest.request())


#value = filedict["data"][0]["priceUsd"].split('.')[0] + "." + filedict["data"][0]["priceUsd"].split('.')[1][:2]
#price = filedict["data"][0]["name"] + " " + value + " $"

coin = "bitcoin"

class CryptoRealm(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 720
        self.top = 480
        self.width = 320
        self.height = 240
        self.UI()
        self.coin = 0
        #self.timer = QtCore.QTimer()
        #self.timer.timeout.connect(self.updateEverything)
        #self.timer.start(1000)


    def UI(self):
        self.setWindowTitle('Crypto Realm')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.button = QPushButton('Coin', self)
        self.button.move(40, 20)
        self.button.clicked.connect(self.askCoin)
        self.cointext = QLabel("No Coin.", self)
        #self.cointext.move(40, 60)
        self.cointext.setGeometry(QtCore.QRect(40,60,100, 80))
        self.show()


    def askCoin(self):
        text, okPressed = QInputDialog.getText(self, "Coin chooser", "Coin name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.coin = text.lower()


    def updateEverything(self):
        if(self.coin != 0):
            coindata = apirequest.searchDBid(self.coin)
            if (coindata != None):
                coinstats = apirequest.price(coindata)
                self.cointext.setText(coinstats)
            else:
                self.cointext.setText("Invalid Coin ID")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CryptoRealm()
    timer = QtCore.QTimer()
    timer.timeout.connect(ex.updateEverything)
    timer.start(500)
    sys.exit(app.exec_())