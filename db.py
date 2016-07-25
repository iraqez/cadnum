# -*- coding: utf-8 -*-

import psycopg2
import ppygis
#import StringIO

import nums
import datacadnum

def dbinsert(cadnum):
    resp = datacadnum.cnum(cadnum)
    conn = psycopg2.connect("host=gis.agro2012.com.ua dbname=agro2012 user=postgres password=workfree")
    cur = conn.cursor()

    s1 = cadnum
    cur.execute('SELECT count(*) FROM cadnum_point where cadnum = %s', (s1,))
    s = cur.fetchone()

    if s[0] == False:
        lat = str(resp.get('lat'))
        lng = str(resp.get('long'))
        cadnum = resp.get('cadnum')
  #      area = resp.get('area')
        geom = ppygis.Point(float(lng), float(lat), srid=4326)

        cur.execute('INSERT INTO cadnum_point(geom, cadnum) VALUES (%s, %s)',(geom, cadnum))
        conn.commit()
        logstr = (u'Номер {} успішно додано в базу!!!'.format(s1))
    else:
        logstr = (u'Номер {} вже існує!!!'.format(s1))


    cur.close()
    conn.close()
    print logstr
    return logstr

if __name__ == '__main__':
   cadnum = raw_input('Вставьте кадастровый номер: ')
   dbinsert(cadnum)
#     for n in nums.cadnums:
#         try:
#             dbinsert(n)
#         except:
#             pass

