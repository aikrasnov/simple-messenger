def test_messages(client):
    response = client.post("/messages/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello"
