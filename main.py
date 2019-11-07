import apirequest
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class CryptoRealm(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 720
        self.top = 480
        self.width = 480
        self.height = 320
        self.coinid = 0
        self.coindata = apirequest.searchDBint(self.coinid)
        self.UI()
        apirequest.updateDB(apirequest.request())

    def setCoinText(self):
        self.cointext = QLabel(self.coinInfo(self.coindata), self)
        self.cointext.setGeometry(QtCore.QRect(120, 120, 240, 80))

    def setSelector(self):
        self.selector = QComboBox(self)
        self.selector.addItems(apirequest.returnNames())
        self.selector.currentIndexChanged.connect(self.coinSelector)
        self.selector.move(160, 80)

    def UI(self):
        self.setWindowTitle('Crypto Realm')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setSelector()
        self.setCoinText()
        self.show()

    def coinSelector(self, i):
        self.coinid = i
        self.coindata = apirequest.searchDBint(self.coinid)
        self.updateEverything()

    @staticmethod
    def coinInfo(data):
        return "Live price: " + apirequest.price(data) + " $\nTraded in the last 24 Hours: " + apirequest.traded24hr \
            (data) + " $\nPrice change in the last 24 Hours: " + apirequest.pricechange \
                   (data) + " %\nAvailable for trading: " + apirequest.supply(data) + " " + data["symbol"]

    def updateEverything(self):
        self.coindata = apirequest.searchDBint(self.coinid)
        self.cointext.setText(self.coinInfo(self.coindata))

    # TODO Track everything related to the coin not just price
    # TODO RED AND GREEN FOR PERCENTAGE
    # TODO Maybe change timing to like 1 minute? and save that and make another file so we can make a chart of the
    # changes

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CryptoRealm()
    timer = QtCore.QTimer()
    timer.timeout.connect(ex.updateEverything)
    timer.start(1500)
    sys.exit(app.exec_())
