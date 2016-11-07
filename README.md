# The Internet of Things project

Started at [a hackathon](http://pripoj.me/cra-iot-hackathon/) by [ČRa](https://www.radiokomunikace.cz/).
If you have a LoRa sensor device with devEUI registered at [pripoj.me](http://pripoj.me/) with an access token,
you can use this application to process the measured data.

Also, if you have an account at [GoSMS](http://www.gosms.cz/), you can send informational SMS.


## Installation

Needed: Python 3

`pip install pip-tools` (once)

`pip-sync requirements*.txt` (keeping the PyPI dependencies up-to-date)


## Configuration

`iot/settings_local.py` skeleton:

```py
TOKEN = ''
DEV_EUI = ''

CAN_SEND_SMS = True
GOSMS = {
    'id': '',
    'secret': '',
    'channel': '',
}

```


## Usage

`./webapp.py [--port PORT]`

The default port is 5000. The webapp is accessible at http://127.0.0.1:5000/ then.


## Testing

`./test.sh`
