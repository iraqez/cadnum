# -*- coding: utf-8 -*-

import psycopg2
import postgis


import datacadnum

def dbinsert(cadnum):
    resp = datacadnum.cnum(cadnum)
    conn = psycopg2.connect("host=agro2012.com.ua dbname=agro2012 user=postgres password=workfree")
    cur = conn.cursor()

    s1 = cadnum
    cur.execute('SELECT count(*) FROM cadnum where cadnum = %s', (s1,))
    s = cur.fetchone()

    if s[0] == False:
        lat = str(resp.get('lat'))
        lng = str(resp.get('long'))
        cadnum = resp.get('cadnum')
        area = resp.get('area')
        geom = postgis.Point(x=lng, y=lat, srid=4326)

        cur.execute('INSERT INTO cadnum(lat, lng, cadnum, area) VALUES (%s, %s, %s, %s)',(lat, lng, cadnum, area))
        conn.commit()
        return ('Number {} like add!!!'.format(s1) )
    else:
        return ('Number {} is present!!!'.format(s1) )

    cur.close()
    conn.close()

if __name__ == '__main__':
    cadnum = raw_input('Вставьте кадастровый номер: ')
    dbinsert(cadnum)