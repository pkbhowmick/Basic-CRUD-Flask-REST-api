import json


def test_hello(app, client):
    res = client.get('/api/hello')
    assert res.status_code == 200
    expected = {'reponse': 'Hello'}
    assert expected == json.loads(res.get_data(as_text=True))