from flask_restx import fields
from ..views import users_ns


"""INPUT MODELS"""
user_model = users_ns.model(
    name="User Login/Sign Up",
    model={
        "email": fields.String(description="User Email", required=True),
        "password": fields.String(description="User Password", required=True),
    },
)

change_password_model = users_ns.model(
    name="User Change Password Model",
    model={
        "old_password": fields.String(description="Old Password", required=True),
        "new_password": fields.String(description="New Password", required=True),
        "confirm_password": fields.String(description="Confirm Password", required=True),}
    )

user_update_model = users_ns.model(
    name="User Update Model",
    model={
        "email": fields.String(description="User Email"),
        "username": fields.String(description="Username"),
    },
)


"""OUTPUT MODELS"""
user_detail_model = users_ns.model(
    name="User Detail Model",
    model={
        "id": fields.Integer(description="User Id"),
        "username": fields.String(description="User Name"),
        "email": fields.String(description="User Email"),
        "is_admin": fields.Boolean(description="Is Admin?"),
        "date_created": fields.DateTime(description="Date Created"),
        "date_modified": fields.DateTime(description="Date Modified"),
    },
)

user_response_model = users_ns.model(
    name="User Response Model",
    model={
        "message": fields.String(description="Response Message"),
        "data": fields.Nested(model=user_detail_model, description="Response Data"),
    },
)

