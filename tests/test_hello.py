import json


def test_index(app, client):
    res = client.get('/hello')
    assert res.status_code == 200
    expected = {'response': 'Hello!'}
    assert expected == json.loads(res.get_data(as_text=True))