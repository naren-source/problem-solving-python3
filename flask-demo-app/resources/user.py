
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from passlib.hash import pbkdf2_sha256

import models
from db import db
from sqlalchemy.exc import SQLAlchemyError
from schemas import UserSchema


blp = Blueprint("Users", "users", description="Operations on users")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if models.UserModel.query.filter(models.UserModel.username == user_data["username"]).first():
            abort(409, message = "A user exists")
        
        user = models.UserModel(
            username = user_data["username"],
            password = pbkdf2_sha256.hash(user_data["password"])
        )
        db.session.add(user)
        db.session.commit()

        return {
            "message": "User Createddd"
        }, 201


@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):        
        user = models.UserModel.query.get_or_404(user_id)
        return user

    def delete(self, user_id):
        user = models.UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User Deleted"}, 200
        
       
        