def test_uptime(test_http_client):
    _, response = test_http_client.get('/uptime')
    assert response.status_code == 200

    # response body check
    expected_data = {
        'status': "ok",
        'environment': 'testing'
    }
    assert response.json == expected_data
