# -*- coding: utf-8 -*-

import psycopg2
import ppygis
import StringIO

import datacadnum

def dbinsert(cadnum):
    resp = datacadnum.cnum(cadnum)
    conn = psycopg2.connect("host=gis.agro2012.com.ua dbname=agro2012 user=postgres password=workfree")
    cur = conn.cursor()

    s1 = cadnum
    cur.execute('SELECT count(*) FROM cadnum where cadnum = %s', (s1,))
    s = cur.fetchone()

    if s[0] == False:
        lat = str(resp.get('lat'))
        lng = str(resp.get('long'))
        cadnum = resp.get('cadnum')
        area = resp.get('area')
        geom = ppygis.Point(float(lng), float(lat), srid=4326)

        cur.execute('INSERT INTO cadnum(geom, lat, lng, cadnum, area) VALUES (%s, %s, %s, %s, %s)',(geom, lat, lng, cadnum, area))
        conn.commit()
        logstr = (u'Номер {} успішно додано в базу!!!'.format(s1))
    else:
        logstr = (u'Номер {} вже існує!!!'.format(s1))
    #     return (u'Number {} like add!!!'.format(s1) )
    # else:
    #     return (u'Number {} is present!!!'.format(s1) )

    cur.close()
    conn.close()
    return logstr

if __name__ == '__main__':
    cadnum = raw_input('Вставьте кадастровый номер: ')
    dbinsert(cadnum)
