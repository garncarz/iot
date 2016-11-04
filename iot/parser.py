# payload documentation:
# http://pripoj.me/jak-spravne-pracovat-s-payloady-zprav/
# http://pripoj.me/wp-content/uploads/2016/08/PayloadDTH_FW0.2.3.pdf

import dateutil.parser
from geopy.geocoders import Nominatim


geolocator = Nominatim()


def _parse(record):
    payload = record['payloadHex']

    b = bytes.fromhex(payload)
    data = {
        'devEUI': record['devEUI'],
        'voltage': b[2] * 100 + b[3],
        'temperature': b[4] + b[5] / 100.0,
        'humidity': b[6] + b[7] / 100.0,
    }
    if b[8] & 1:
        data['temperature'] = -data['temperature']

    data['datetime'] = dateutil.parser.parse(record['createdAt'])

    data['location'] = geolocator.reverse('{lrrLAT}, {lrrLON}'.format(**record))

    return data


def parse(record):
    try:
        return _parse(record)
    except IndexError:
        return None
