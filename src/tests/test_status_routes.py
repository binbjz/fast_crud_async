def test_status_check(test_app):
    response = test_app.get("/status_check")
    assert response.status_code == 200
    assert response.json() == {"verify": "success!"}
