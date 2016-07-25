# -*- coding: utf-8 -*-

from PyQt4.QtSql import *

import datacadnum

def dbinsert(cadnum):
  #  resp = datacadnum.cnum(cadnum)


    db = QSqlDatabase.addDatabase("QPSQL")
    db.setHostName("gis.agro2012.com.ua")
    db.setPort(5432)
    # non spatial table or view
    db.setDatabaseName("agro2012")
    db.setUserName("postgres")
    db.setPassword("workfree")
    db.open()

    s1 = cadnum
    query = QSqlQuery(db)

  #  cnInBase = 'SELECT count(*) FROM cadnum_point where cadnum = %s', (s1,)
    query.exec_("""
    SELECT count(*) FROM cadnum_point where cadnum = '%s'
    """ % (s1))
      # SELECT cadnum, area, st_ymax, purpose, parcel, lat, zona, st_ymin, ownershipvalue,
      #  ownershipcode, st_xmin, st_xmax, lng, koatuu, id_office, use,
      #  kvartal, unit_area
      # FROM cadnum;

    while query.next():
        if unicode(query.value(0).toString()) == 0:
            lat = str(resp.get('lat'))
            lng = str(resp.get('long'))
            cadnum = resp.get('cadnum')

        else:
            logstr = (u'Номер {} вже існує!!!'.format(s1))

if __name__ == '__main__':
    #dbinsert(cadnum)
    cadnum = raw_input('Вставьте кадастровый номер: ')
    dbinsert(cadnum)
    # for n in nums.cadnums:
    #         try:
    #             dbinsert(n)
    #         except:
    #             pass