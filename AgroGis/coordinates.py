#import datacadnum
import math

def addCoordinates(resp):
#    resp = datacadnum.resp
    ymin = float(resp['st_ymin'])
    xmin = float(resp['st_xmin'])
    ymax = float(resp['st_ymax'])
    xmax = float(resp['st_xmax'])

    long = (xmin+(xmax-xmin)/2-0.0017)/(math.pi/180) / 6378137
    lat = (2*math.atan(math.exp((ymin+(ymax-ymin)/2-0.0002)/6378137))-math.pi/2)/(math.pi/180)
    coordinates = {'lat': lat, 'long': long}
    resp.update(coordinates)
    return resp


