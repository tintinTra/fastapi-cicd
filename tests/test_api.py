import pytest
from fastapi.testclient import TestClient

import fastapi_cicd


@pytest.fixture
def client(monkeypatch):
    # Jeder Test erhält einen eigenen Speicher.
    monkeypatch.setattr(fastapi_cicd, "db", {})
    with TestClient(fastapi_cicd.app) as client:
        yield client


@pytest.fixture
def book():
    return {
        "title": "Dune",
        "isbn": "9780441172719",
        "author": "Frank Herbert",
    }


def test_status(client):
    response = client.get("/status")

    assert response.status_code == 200
    assert response.json() == {"status": 200}


def test_create_book(client, book):
    response = client.post("/book", json=book)

    assert response.status_code == 200
    assert response.json() == book
    assert fastapi_cicd.db[book["isbn"]] == book


def test_create_books(client, book):
    second_book = {
        "title": "1984",
        "isbn": "9780451524935",
        "author": "George Orwell",
    }
    books = [book, second_book]

    response = client.post("/books", json=books)

    assert response.status_code == 200
    assert response.json() == books
    assert set(fastapi_cicd.db) == {item["isbn"] for item in books}
    for item in books:
        stored = fastapi_cicd.db[item["isbn"]]
        assert stored.model_dump() == item


def test_reject_book_without_isbn(client, book):
    del book["isbn"]

    response = client.post("/book", json=book)

    assert response.status_code == 422
    assert fastapi_cicd.db == {}


def test_reject_invalid_batch(client, book):
    response = client.post(
        "/books",
        json=[book, {"title": "Incomplete"}],
    )

    assert response.status_code == 422
    assert fastapi_cicd.db == {}
