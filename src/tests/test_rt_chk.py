def test_route_check(test_app):
    response = test_app.get("/rt_chk")
    assert response.status_code == 200
    assert response.json() == {"verify": "success!"}
