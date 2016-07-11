# -*- coding: utf-8 -*-

import json, requests
import coordinates
url_point = 'http://212.26.144.110/kadastrova-karta/find-Parcel'
url_data = 'http://212.26.144.110/kadastrova-karta/get-parcel-Info'

#cadnum='0524587000:01:003:0358'
def cnum(cadnum):

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
    coordinates.addCoordinates(resp)
    return resp



if __name__ == '__main__':
    cadnum = raw_input('Вставьте кадастровый номер: ')
    resp = cnum(cadnum)
    try:
        print(resp)
    except:
        print("Нет данных по {}".format(cadnum))