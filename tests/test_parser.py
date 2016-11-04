from iot.parser import parse


def test_parse_by_doc():
    data = parse({'payloadHex': '2408200315143C1E00'})
    assert data['voltage'] == 3203  # mV
    assert data['temperature'] == 21.20  # °C
    assert data['humidity'] == 60.30  # %
