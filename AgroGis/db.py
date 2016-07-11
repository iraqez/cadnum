import psycopg2
import postgis


import datacadnum

cd = datacadnum.resp
conn = psycopg2.connect("host=agro2012.com.ua dbname=agro2012 user=postgres password=workfree")
cur = conn.cursor()

s1 = datacadnum.params_point.get('cadnum')
cur.execute('SELECT count(*) FROM cadnum where cadnum = %s', (s1,))
s = cur.fetchone()

if s[0] == False:
    lat = str(datacadnum.resp.get('lat'))
    lng = str(datacadnum.resp.get('long'))
    cadnum = datacadnum.resp.get('cadnum')
    area = datacadnum.resp.get('area')
    geom = postgis.Point(x=lng, y=lat, srid=4326)

    cur.execute('INSERT INTO cadnum(geom, lat, lng, cadnum, area) VALUES (%s, %s, %s, %s, %s)',(geom, lat, lng, cadnum, area))
    conn.commit()
    print('Номер {} успешно добавлен!!!'.format(s1) )
else:
    print('Номер {} существует в базе!!!'.format(s1) )

cur.close()
conn.close()