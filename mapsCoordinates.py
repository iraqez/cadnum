# OurApp.py

from PyQt4.QtGui import *
from qgis.core import *

from ourmainwindow import OurMainWindow

app = QApplication([])
# set up QGIS
QgsApplication.setPrefixPath('/usr', True)
QgsApplication.initQgis()

# set the main window and show it
mw = OurMainWindow()
mw.show()

app.exec_()

mw = None
# clean up QGIS
QgsApplication.exitQgis()

#ourmainwindow.py

import os

from PyQt4.QtGui import *

from qgis.gui import *
from qgis.core import *

import resources
from PyQt4.QtGui import QAction, QMainWindow
from PyQt4.QtCore import SIGNAL, Qt

import sys, os


  from lxml.html.builder import CENTER
  from PyQt4.QtCore import SIGNAL, Qt, QString

  class OurMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setupGui()

    self.add_ogr_layer('/data/alaska.shp')
    self.map_canvas.zoomToFullExtent()
    mCanvas = QgsMapCanvas()
    self.map_canvas = mCanvas


#def canvasPressEvent(self, e):
#    self.startPoint = self.toMapCoordinates(e.pos())
#    self.endPoint = self.startPoint
#    self.isEmittingPoint = True
#    self.showRect(self.startPoint, self.endPoint)

def setupGui(self):
    frame = QFrame(self)
    self.setCentralWidget(frame)
    self.grid_layout = QGridLayout(frame)

    self.map_canvas = QgsMapCanvas()
    extentBox = self.map_canvas.extent()
    xCoMin = extentBox.xMinimum()
    xCoM = extentBox.xMaximum()

    self.map_canvas.setCanvasColor(QColor(255, 255, 255))
    self.grid_layout.addWidget(self.map_canvas)

    # setup action(s)
    self.zoomin_action = QAction(
        QIcon(":/ourapp/zoomin_icon"),
        "Zoom In",
        self)

    self.identify2_action = QAction( QString("GetCoordinates tool"), self)
    self.identify2_action.setCheckable(True)
    self.identify2_action.setChecked(True)
    # create toolbar
    self.toolbar = self.addToolBar("Map Tools")
    self.toolbar.addAction(self.identify2_action)
    self.identify2_action.setCheckable(True)


    # connect the tool(s)

    self.identify2_action.triggered.connect(self.identify2)

                    # create the map tool(s)

    self.tool_identify2 = QgsMapToolIdentify(self.map_canvas)

def add_ogr_layer(self, path):
    #(name, ext) = os.path.basename(path).split('.')
    #layer = QgsVectorLayer(path, name, 'ogr')
    #QgsMapLayerRegistry.instance().addMapLayer(layer)
    layer = QgsVectorLayer('/home/Documents/Data/pyqgis_data/alaska.shp','alaska','ogr')
    QgsMapLayerRegistry.instance().addMapLayer(layer)

    canvas_layer = QgsMapCanvasLayer(layer)
    self.map_canvas.setLayerSet([canvas_layer])

def identify2(self):
    #self.map_canvas.setMapTool(self.tool_zoomin)
    mCanvas = self.map_canvas
    self.canvas = mCanvas
    QgsMapToolEmitPoint.__init__(self, self.canvas)
    #RectangleMapTool(mCanvas)
    #PointTool(mCanvas)
    tool = PointTool(self.map_canvas)
    self.map_canvas.setMapTool(tool)
    #tool = PointTool(self, self.map_canvas)
    #QMessageBox.warning(None, test2)
class PointTool(QgsMapTool):
def init(self, canvas): QgsMapTool.init(self, canvas) self.canvas = canvas

def canvasPressEvent(self, event):
    x = event.pos().x()
    y = event.pos().y()