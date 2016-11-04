from datetime import datetime

import pytest

from iot.parser import parse


saved_records = [
    {
        'aDRbit': 0,
        'channel': 'LC2',
        'createdAt': '2016-11-04T11:20:53+0000',
        'devEUI': '00wonttell',  # changed
        'devLrrCnt': 2,
        'fCntDn': 3,
        'fCntUp': 1949,
        'fPort': 1,
        'lrrLAT': 50.079865,
        'lrrLON': 14.375842,
        'lrrRSSI': -107,
        'lrrSNR': -4.75,
        'lrrid': '290000F5',
        'lrrs': [
            {'LrrESP': -113.0047,
             'LrrRSSI': -107,
             'LrrSNR': -4.75,
             'Lrrid': '290000F5'},
            {'LrrESP': -125.864044,
             'LrrRSSI': -110,
             'LrrSNR': -15.75,
             'Lrrid': '2900000E'},
        ],
        'micHex': '',
        'payloadHex': '0706202b1446153c00',
        'spFact': 12,
        'subBand': 'G1',
    },
    {
        'aDRbit': 0,
        'channel': 'LC3',
        'createdAt': '2016-11-03T12:20:19+0000',
        'devEUI': '00wonttell',  # changed
        'devLrrCnt': 2,
        'fCntDn': 3,
        'fCntUp': 1926,
        'fPort': 1,
        'lrrLAT': 50.079845,
        'lrrLON': 14.375819,
        'lrrRSSI': -100,
        'lrrSNR': -12.25,
        'lrrid': '290000F5',
        'lrrs': [
            {'LrrESP': -112.501282,
             'LrrRSSI': -100,
             'LrrSNR': -12.25,
             'Lrrid': '290000F5'},
            {'LrrESP': -112.972855,
             'LrrRSSI': -109,
             'LrrSNR': -1.75,
             'Lrrid': '290000C0'},
        ],
        'micHex': '',
        'payloadHex': '070620211428123c00',
        'spFact': 12,
        'subBand': 'G1',
    },
]


def test_parse():
    data = parse({
        'payloadHex': '2408200315143C1E00',  # from documentation
        'createdAt': '2016-11-03T12:20:19+0000',
        'lrrLAT': 50.079845,
        'lrrLON': 14.375819,
    })
    assert data['voltage'] == 3203  # mV
    assert data['temperature'] == 21.20  # °C
    assert data['humidity'] == 60.30  # %
    assert data['datetime'].replace(tzinfo=None) \
            == datetime(2016, 11, 3, 12, 20, 19)
    assert 'Praha' in data['location'].address


@pytest.mark.parametrize('record', saved_records)
def test_parse_saved(record):
    data = parse(record)
    assert -20 < data['temperature'] < 50
    assert 5 < data['humidity'] < 90
