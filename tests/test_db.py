from sqlalchemy import select

from fast_zero.models import User


# 45:03'
def test_create_user(session):
    user = User(
        username='test', email='test@test.com', password='testpassword'
    )

    session.add(user)
    session.commit()
    # session.refresh(user)

    result = session.scalar(select(User).where(User.email == 'test@test.com'))

    assert result.id == 1
    assert result.username == 'test'
    assert result.email == 'test@test.com'
