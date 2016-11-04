from grab import Grab

from . import settings


URL = 'https://api.pripoj.me/message/get/{dev_eui}?token={token}'


def get(dev_eui=getattr(settings, 'DEV_EUI'),
        token=getattr(settings, 'TOKEN')):
    g = Grab()
    resp = g.go(URL.format(dev_eui=dev_eui, token=token))
    return resp.json
