# -*- coding: utf-8 -*-
import csv
import psycopg2
import ppygis
import datacadnum

def dbinsert(cadnum):

    conn = psycopg2.connect("host=gis.agro2012.com.ua dbname=agro2012 user=postgres password=workfree")
    cur = conn.cursor()

    s1 = cadnum
    cur.execute('SELECT count(*) FROM cadnum where cadnum = %s', (s1,))
    s = cur.fetchone()

    if s[0] == False:
        resp = datacadnum.cnum(cadnum)
        cadnum = str(resp.get(u'cadnum'))
        area = str(resp.get(u'area'))
        st_ymax = str(resp.get(u'st_ymax'))
        purpose = unicode(resp.get(u'purpose'))
        parcel = str(resp.get(u'parcel'))
        lat = str(resp.get(u'lat'))
        zona = str(resp.get(u'zona'))
        st_ymin = str(resp.get(u'st_ymin'))
        ownershipvalue = str(resp.get(u'ownershipvalue'))
        ownershipcode = str(resp.get(u'ownershipcode'))
        st_xmin = str(resp.get(u'st_xmin'))
        st_xmax = str(resp.get(u'st_xmax'))
        lng = str(resp.get(u'lng'))
        koatuu = str(resp.get(u'koatuu'))
        id_office = str(resp.get(u'id_office'))
        use = unicode(resp.get(u'use'))
        kvartal = str(resp.get(u'kvartal'))
        unit_area = unicode(resp.get(u'unit_area'))

        # lat = str(resp.get('lat'))
        # lng = str(resp.get('long'))
        # cadnum = resp.get('cadnum')
  #      area = resp.get('area')
        geom = ppygis.Point(float(lng), float(lat), srid=4326)

#        cur.execute('INSERT INTO cadnum_point(geom, cadnum) VALUES (%s, %s)',(geom, cadnum))
        cur.execute("""
            INSERT INTO cadnum(cadnum, area, st_ymax, purpose, parcel, lat, zona, st_ymin,
              ownershipvalue, ownershipcode, st_xmin, st_xmax, lng, koatuu, id_office, use,
              kvartal, unit_area)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s, %s,
              %s, %s)""", (cadnum, area, st_ymax, purpose, parcel, lat, zona, st_ymin,
              ownershipvalue, ownershipcode, st_xmin, st_xmax, lng, koatuu, id_office, use,
              kvartal, unit_area))
        cur.execute('INSERT INTO cadnum_point(geom, cadnum) VALUES (%s, %s)', (geom, cadnum))
        conn.commit()
        logstr = (u'Номер {} успішно додано!!!'.format(s1))
    else:
        logstr = (u'Номер {} вже існує!!!'.format(s1))


    cur.close()
    conn.close()
 #   print logstr
    return logstr

if __name__ == '__main__':
#   cadnum = raw_input(u'Вставьте кадастровый номер: ')
#   dbinsert(cadnum)
#---------------------------------------------------------------
    with open("/home/iraqez/agro2012.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                dbinsert(row[0])
            except:
                print row
                pass

#---------------------------------------------------------------
#     for n in nums.cadnums:
#         try:
#             dbinsert(n)
#         except:
#             pass

