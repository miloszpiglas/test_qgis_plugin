from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *

class Plugin(object):

    def __init__(self,iface):
        self.iface = iface
    
    def initGui(self):
        self.qgisAction = QAction("Test plugin", self.iface.mainWindow())
        self.qgisAction.setWhatsThis("Test plugin")
        self.qgisAction.setStatusTip("Test plugin")
        self.qgisAction.triggered.connect(self.run)

        self.iface.addToolBarIcon(self.qgisAction)
        self.iface.addPluginToMenu("Test plugin",self.qgisAction)

    def unload(self):
        return
        
    def run(self):
        panel = MainPanel(self.iface.mainWindow())
        self.iface.addDockWidget( Qt.RightDockWidgetArea, panel )

class MainPanel(QDockWidget):

    def __init__(self, parent=None):
        QDockWidget.__init__(self, parent=parent)
        wgt = QWidget()
        lay = QVBoxLayout(self)
        self.status = QStatusBar(self)
        btn = QPushButton('X')
        self._listWgt = QListWidget(self)
        self._listWgt.addItems(['aaa', 'bbbb', 'cccc', 'dddd'])
        self.status.showMessage('INIT ok')
        self._listWgt.itemClicked.connect(self.selected)
        btn.pressed.connect(self.pres)
        
        # btn.clicked.connect(lambda x: self.not_existing_method(x))

        lay.addWidget(btn)
        lay.addWidget(self._listWgt)
        lay.addWidget(self.status)
        wgt.setLayout(lay)
        self.setWidget(wgt)

    def pres(self):
        self.status.showMessage('pres')
        raise Exception('wrong method')
    
    def selected(self, x):
        QgsMessageLog.logMessage('hi: ' + x.text(), 'Test plugin', level=Qgis.Info)
        self.status.showMessage(x.text())

def start(parent, iface=None, app=None):
    log = None
    if iface:
        log = QgsLogAdapter('Asquare')
    else:
        log = StdOutLogAdapter()
    panel = MainPanel(log, parent)
    if iface:
        iface.currentLayerChanged.connect(panel.printLayer)
        iface.addDockWidget( Qt.RightDockWidgetArea, panel )
    elif app:
        window = QMainWindow()
        window.setCentralWidget(panel)
        window.show()
        app.exec_()

def main():
    from sys import argv
    app = QApplication(argv)
    start(None, None, app)

if __name__ == '__main__':
    main()
