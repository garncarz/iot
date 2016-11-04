from iot import crawler


def test_get():
    resp = crawler.get()
    assert '_meta' in resp
    assert resp['_meta']['status'] == 'SUCCESS'
    assert 'records' in resp
