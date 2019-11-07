

import apirequest
import sys
 
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
 
class CryptoRealm(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 720
        self.top = 480
        self.width = 320
        self.height = 240
        self.UI()
        self.coin = 0
 
 
    def UI(self):
        self.setWindowTitle('Crypto Realm')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.button = QPushButton('Coin', self)
        self.button.move(40, 20)
        self.button.clicked.connect(self.askCoin)
        self.cointext = QLabel("No Coin.", self)
        self.cointext.setGeometry(QtCore.QRect(40, 60, 100, 80))
        self.show()
 
 
    def askCoin(self):
        text, okPressed = QInputDialog.getText(self, "Coin chooser", "Coin name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.coin = text.lower()
 
 
    def updateEverything(self):
        if(self.coin != 0):
            coindata = apirequest.searchDBid(self.coin)
            if (coindata != None):
                coinstats = apirequest.price(coindata) + "\n" + apirequest.pricechange(coindata) +"\n" + apirequest.traded24hr(coindata)
                self.cointext.setText(coinstats)
            else:
                self.cointext.setText("Invalid Coin ID")
 
    #TODO Track everything related to the coin not just price
    #TODO Search bar for the coins
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CryptoRealm()
    timer = QtCore.QTimer()
    timer.timeout.connect(ex.updateEverything)
    timer.start(300)
    sys.exit(app.exec_())
