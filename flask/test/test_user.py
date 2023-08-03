import json
from src.main import app
from src.database import db_session
from src.models.user import User


class TestUser:
    def setup_class(self):
        pass

    def test_create_user(self):
        with app.test_client() as client:
            response = client.post(
                "http://localhost/user/", json={"name": "Name", "email": "Email"}
            )
            assert response.status_code == 201

            response = client.get("http://localhost/user/")
            assert response.status_code == 200

            result = json.loads(response.data.decode("utf-8"))
            assert len(result) == 1
            assert result[0]["name"] == "Name"
            assert result[0]["email"] == "Email"

    def destroy_all(db_class):
        db_session.query(db_class).delete()
        db_session.commit()

    def teardown_class(self):
        self.destroy_all(User)
