

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
        self.coinid = 0
        self.coindata = apirequest.searchDBint(self.coinid)
        self.UI()
        apirequest.updateDB(apirequest.request())
 

    def setCoinText(self):
        self.cointext = QLabel(self.coinInfo(self.coindata), self)
        self.cointext.setGeometry(QtCore.QRect(50, 90, 240, 80))
        #self.cointext.move(70, 80)


    def UI(self):
        #layout = QHBoxLayout()
        self.setWindowTitle('Crypto Realm')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.selector = QComboBox(self)
        self.selector.addItems(apirequest.returnNames())
        self.selector.currentIndexChanged.connect(self.coinSelector)
        self.selector.move(90, 60)
        self.setCoinText()
        self.show()
 

    def coinSelector(self, i):
        self.coinid = i
        self.coindata = apirequest.searchDBint(self.coinid)
        self.updateEverything()


    def coinInfo(self, data):
        return "Live price: " + apirequest.price(data) + " $\nTraded in the last 24 Hours: " + apirequest.traded24hr(data) + " $\nPrice change in the last 24 Hours: " + apirequest.pricechange(data) + " %\nAvailable for trading: " + apirequest.supply(data) + " " + data["symbol"]


    def updateEverything(self):
        self.coindata = apirequest.searchDBint(self.coinid)
        self.cointext.setText(self.coinInfo(self.coindata))

 
    #TODO Track everything related to the coin not just price
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CryptoRealm()
    timer = QtCore.QTimer()
    timer.timeout.connect(ex.updateEverything)
    timer.start(1500)
    sys.exit(app.exec_())