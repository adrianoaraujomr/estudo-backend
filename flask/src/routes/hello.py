import os
from flask import Blueprint, Response
from dotenv import load_dotenv

hello_route = Blueprint("hello", __name__)
load_dotenv()

HELLO_MESSAGE = os.getenv("HELLO_WORLD_MESSAGE")


@hello_route.route("/")
def hello_world_en():
    return Response(HELLO_MESSAGE, status=200, mimetype="text/plain")
