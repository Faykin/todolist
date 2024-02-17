
from debugpy import connect
from fastapi.testclient import TestClient
from .main import app
import redis

client = TestClient(app)


## testing the root

def test_read_main():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"Hello":"World"}

# testing the todos

data = {
    "title": "Daniel Faykin",
    "due_date": "Today",
    "description": "This is for testing"
}

def test_create_todo():
    res = client.post("/todo/", json=data)
    print(20*"=", res)
    assert res.status_code == 200
    assert res.json() == []

def test_get_all_todo():
    res = client.get("/todo/", json=data)
    assert res.status_code == 200
    assert data in res.json()

def test_get_todo():
    res = client.get("/todo/0")
    assert res.status_code == 200
    # assert res.json() == data

def test_update_todo():
    res = client.put("/todo/0", json = data)
    assert res.status_code == 200
    assert res.json() == data

def test_delete_todo():
    response = client.delete("/todo/0")
    assert response.status_code == 200
    assert response.json() == {}

def test_connect_redis():
    connection = redis.StrictRedis(host='docker.for.mac.localhost', port=6379)
    assert connection.ping() == True