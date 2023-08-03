from flask import Flask
from src.database import db_session, init_db
from src.routes.hello import hello_route
from src.routes.user import user_route

app = Flask(__name__)
app.register_blueprint(hello_route, url_prefix="/hello")
app.register_blueprint(user_route, url_prefix="/user")

init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
