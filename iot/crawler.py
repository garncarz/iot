# REST API documentation:
# http://pripoj.me/summer-jam-rest-api/

from grab import Grab

from . import settings, parser


URL = 'https://api.pripoj.me/message/get/{dev_eui}?token={token}&limit={limit}'


def get(dev_eui=getattr(settings, 'DEV_EUI', None),
        token=getattr(settings, 'TOKEN', None),
        limit=100):
    g = Grab()
    resp = g.go(URL.format(dev_eui=dev_eui, token=token, limit=limit))
    return resp.json


def get_last_record():
    batch = get(limit=settings.MAX_TRIES)
    for rec_raw in batch['records']:
        rec = parser.parse(rec_raw)
        if rec:
            return rec


def get_many_records():
    batch = get(limit=settings.MANY_RECORDS)
    return filter(lambda rec: rec, map(parser.parse, batch['records']))
