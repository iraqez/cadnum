from qgis.core import *

QgsApplication.setPrefixPath("/usr/bin/qgis", True)
qgs = QgsApplication([], False)
qgs.initQgis()

uri = QgsDataSourceURI()
uri.setConnection("gis.agro2012.com.ua", "5432", "agro2012", "postgres", "workfree")
uri.setDataSource("public", "agro2012")

vlayer = QgsVectorLayer(uri.uri(), "cadnum_point", "postgres")