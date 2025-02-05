from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_ready_root_deve_retornar_ok():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundod!'}  # Assert
