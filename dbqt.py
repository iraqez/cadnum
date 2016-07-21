from PyQt4.QtSql import *

import datacadnum

def dbinsert(cadnum):
    resp = datacadnum.cnum(cadnum)


    db = QSqlDatabase.addDatabase("QPSQL")
    db.setHostName("gis.agro2012.com.ua")
    db.setPort(5432)
    # non spatial table or view
    db.setDatabaseName("agro2012")
    db.setUserName("postgres")
    db.setPassword("workfree")

    s1 = cadnum
    query = QSqlQuery(db)

    cnInBase = ""
    query.exec_("""

    """)