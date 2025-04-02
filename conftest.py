import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from fast_zero.app import app
from fast_zero.database import get_session
from fast_zero.models import User, table_registry
from fast_zero.security import get_password_hash


@pytest.fixture
def client(session):
    # Retorna a sessão de teste
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override

        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    # Conexão com bd
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    # Cria a tabela no banco de dados
    table_registry.metadata.create_all(engine)

    # Fornece uam instância de Session para os testes via yield session
    with Session(engine) as session:
        yield session

    # Após os testes exclui as tabelas
    table_registry.metadata.drop_all(engine)


@pytest.fixture
def user(session):
    pwd = 'testpassword'

    user = User(
        username='testusername',
        email='test@email.com',
        password=get_password_hash(pwd)
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = pwd  # Monkey Patch

    return user
