import pytest

from iot import crawler, settings


@pytest.mark.skipif(not hasattr(settings, 'DEV_EUI'),
                    reason='No device registered.')
def test_get():
    resp = crawler.get()
    assert '_meta' in resp
    assert resp['_meta']['status'] == 'SUCCESS'
    assert 'records' in resp
