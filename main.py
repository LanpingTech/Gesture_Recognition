import sys
from mainWidget import *
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)


app = QApplication(sys.argv)
myWin = MyMainWindow()
#窗口置于屏幕中央
myWin.move((QDesktopWidget().availableGeometry().width() - myWin.width()) // 2,
           (QDesktopWidget().availableGeometry().height() - myWin.height()) // 2)
myWin.show()
sys.exit(app.exec_())
