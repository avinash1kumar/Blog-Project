def test_get_blogs(client):
    response = client.get("/blogs")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2
    assert data[0]["title"] == "Python"
    assert data[1]["title"] == "FastAPI"
    

def test_get_single_blog(client):
    response = client.get("/blogs/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Python"
    
def test_blog_not_found(client):
    response = client.get("/blogs/999")

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Blog not found"
    }
    

def test_create_blog(client):
    payload = {
        "title": "Pytest",
        "content": "Learn automated testing"
    }

    response = client.post("/blogs", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Pytest"
    assert data["content"] == "Learn automated testing"
    assert "id" in data
    

def test_create_blog_invalid_data(client):
    payload = {
        "content": "Learn automated testing"
    }

    response = client.post("/blogs", json=payload)

    assert response.status_code == 422