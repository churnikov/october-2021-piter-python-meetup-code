from app.api import app

TEST_CLIENT = app.test_client()


def test_add_data():
    resp = TEST_CLIENT.post("/v0/add-data", json={"data": "data"})
    assert resp.status_code == 200
    assert resp.json == {"result": "success"}
