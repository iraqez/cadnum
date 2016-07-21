# -*- coding: utf-8 -*-

import json, requests
import re
import math

def addCoordinates(resp):
#    resp = datacadnum.resp
    ymin = float(resp['st_ymin'])
    xmin = float(resp['st_xmin'])
    ymax = float(resp['st_ymax'])
    xmax = float(resp['st_xmax'])

    lng = (xmin+(xmax-xmin)/2-0.0017)/(math.pi/180) / 6378137
    lat = (2*math.atan(math.exp((ymin+(ymax-ymin)/2-0.0002)/6378137))-math.pi/2)/(math.pi/180)
    coordinates = {'lat': lat, 'lng': lng}
    resp.update(coordinates)
    return resp

url_point = 'http://212.26.144.110/kadastrova-karta/find-Parcel'
url_data = 'http://212.26.144.110/kadastrova-karta/get-parcel-Info'

#cadnum='0524587000:01:003:0358 '
def cnum(cadnum):
    re.sub(r'\s', '', cadnum)
    params_point = dict(
        cadnum=cadnum,
    )

    resp = (json.loads(requests.get(url=url_point, params=params_point).text)['data'])[0]
    params_data = dict(
        koatuu=cadnum.split(':')[0],
        zone=cadnum.split(':')[1],
        quartal=cadnum.split(':')[2],
        parcel=cadnum.split(':')[3],
    )
    resp.update((json.loads(requests.get(url=url_data, params=params_data).text)['data'])[0])
    addCoordinates(resp)
    try:
        return resp
    except:
        notCN = ("Нет данных по {}".format(cadnum))
        return notCN


if __name__ == '__main__':
    cadnum = raw_input('Вставьте кадастровый номер: ')
    resp = cnum(cadnum)
    try:
        print(resp)
    except:
        print("Нет данных по {}".format(cadnum))