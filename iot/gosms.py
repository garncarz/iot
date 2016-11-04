import json

from grab import Grab
from unidecode import unidecode

from . import settings


TOKEN_URL = 'https://app.gosms.cz/oauth/v2/token'
SEND_URL = 'https://app.gosms.cz/api/v1/messages/'


def squeeze(text):
    return ''.join([part.capitalize() for part in text.split()])

f_squeeze = squeeze


def send(msg, recipients=getattr(settings, 'PHONE_DEST'), squeeze=False):
    g = Grab()
    resp_token = g.go(TOKEN_URL,
                      post={
                        'client_id': settings.GOSMS['id'],
                        'client_secret': settings.GOSMS['secret'],
                        'grant_type': 'client_credentials',
                      })
    token = resp_token.json['access_token']

    msg = unidecode(msg.strip())
    if squeeze:
        msg = f_squeeze(msg)

    response = g.go(SEND_URL,
                    headers={'Authorization': 'Bearer %s' % token},
                    post=json.dumps({
                        'message': msg,
                        'recipients': recipients,
                        'channel': settings.GOSMS['channel'],
                    }))
