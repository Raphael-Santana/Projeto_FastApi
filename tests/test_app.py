from http import HTTPStatus

from fastapi.testclient import TestClient

from projeto_fastapi.app import app


def test_read_root_deve_retornar_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get("/")  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (garantir)
    assert response.json() == "Olá Mundo"
