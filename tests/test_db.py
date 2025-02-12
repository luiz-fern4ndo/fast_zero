from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='luiz',
        email='luiz@luiz.com',
        password='minha_senha-legal',
    )

    # session.refresh(user)
    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'luiz@luiz.com'))

    assert result.username == 'luiz'
