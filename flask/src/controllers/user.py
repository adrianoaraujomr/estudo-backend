from src.database import db_session
from src.models.user import User


def list_users():
    users = User.query.all()
    return [{"id": user.id, "name": user.name, "email": user.email} for user in users]


def get_user_by_id(id):
    try:
        user = User.query.filter_by(id=int(id)).first()
        return {"id": user.id, "name": user.name, "email": user.email}
    except:
        raise Exception("User don't exist")


def create_user(content):
    new_user = User(content["name"], content["email"])
    db_session.add(new_user)
    db_session.commit()
    return content


def update_user(id, content):
    try:
        user = User.query.filter_by(id=int(id)).first()
        user.name = content["name"]
        user.email = content["email"]
        db_session.add(user)
        db_session.commit()
        return content
    except:
        raise Exception("User don't exist")


def delete_user(id):
    try:
        user = User.query.filter_by(id=int(id)).first()
        db_session.delete(user)
        db_session.commit()
    except:
        raise Exception("User don't exist")
