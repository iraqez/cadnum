# -*- coding: utf-8 -*-

#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

app = QApplication(sys.argv)


web = QWebView()
web.resize(980, 600)
title = unicode(u"Кадастрова карта")
web.setWindowTitle(title)
web.load(QUrl("http://map.land.gov.ua/kadastrova-karta/"))
web.show()

sys.exit(app.exec_())