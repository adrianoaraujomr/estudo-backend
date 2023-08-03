import json
from flask import Blueprint, Response, request
from src.controllers.user import (
    list_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
)

user_route = Blueprint("user", __name__)


@user_route.route("/")
def list_users_route():
    result = list_users()
    return Response(json.dumps(result), status=200, mimetype="application/json")


@user_route.route("/<id>")
def get_user_by_id_route(id):
    try:
        result = get_user_by_id(id)
        return Response(json.dumps(result), status=200, mimetype="application/json")
    except:
        return Response("User don't exist", status=404)


@user_route.route("/", methods=["POST"])
def create_user_route():
    content = request.json
    result = create_user(content)
    return Response(json.dumps(result), status=201, mimetype="application/json")


@user_route.route("/<id>", methods=["PUT"])
def update_user_route(id):
    try:
        content = request.json
        result = update_user(id, content)
        return Response(json.dumps(result), status=200, mimetype="application/json")
    except:
        return Response("User don't exist", status=404)


@user_route.route("/<id>", methods=["DELETE"])
def delete_user_route(id):
    try:
        delete_user(id)
        return Response("", status=200)
    except:
        return Response("User don't exist", status=404)
