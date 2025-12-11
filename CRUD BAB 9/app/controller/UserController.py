from app.models.user import Users
from app import response, app
from flask import request
from app import db
import traceback


def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print("ERROR index():", e)
        traceback.print_exc()
        return response.badRequest([], "Internal Server Error")


def transform(users):
    array = []
    for i in users:
        array.append({
            "id": i.id,
            "name": i.name,
            "email": i.email
        })
    return array


def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], "User not found")

        data = singleTransform(users)
        return response.ok(data, "")
    except Exception as e:
        print("ERROR show():", e)
        traceback.print_exc()
        return response.badRequest([], "Internal Server Error")


def singleTransform(users):
    return {
        "id": users.id,
        "name": users.name,
        "email": users.email
    }


def store():
    try:
        name = request.json.get("name")
        email = request.json.get("email")
        password = request.json.get("password")

        if not name or not email or not password:
            return response.badRequest([], "Missing required field")

        users = Users(name=name, email=email)
        users.setPassword(password)

        db.session.add(users)
        db.session.commit()

        return response.ok("", "Successfully created data!")
    except Exception as e:
        print("ERROR store():", e)
        traceback.print_exc()
        return response.badRequest([], str(e))


def update(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], "User not found")

        name = request.json.get("name")
        email = request.json.get("email")
        password = request.json.get("password")

        user.name = name if name else user.name
        user.email = email if email else user.email

        if password:
            user.setPassword(password)

        db.session.commit()

        return response.ok("", "Successfully updated data!")
    except Exception as e:
        print("ERROR update():", e)
        traceback.print_exc()
        return response.badRequest([], str(e))


def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], "User not found")

        db.session.delete(user)
        db.session.commit()

        return response.ok("", "Successfully deleted data!")
    except Exception as e:
        print("ERROR delete():", e)
        traceback.print_exc()
        return response.badRequest([], "Internal Server Error")
