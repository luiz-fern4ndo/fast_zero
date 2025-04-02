from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'test',
            'email': 'test@test.com',
            'password': 'testpassword',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'test',
        'email': 'test@test.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'testpassword',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@test.com',
    }


# def test_delete_user(client):
#     response = client.delete('/users/1')

#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {'message': 'User deleted'}


def test_update_should_return_not_found_exercice(client):
    response = client.put(
        '/users/100',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'testpassword',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_should_return_not_found_exercice(client):
    response = client.delete('/users/100')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_token(client, user):
    response = client.post(
        '/token',
        data={'username': user.email, 'password': user.clean_password}
    )

    token = response.json()
    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'Bearer'
    assert 'access_token' in token
