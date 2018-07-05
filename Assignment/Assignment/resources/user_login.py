from flask_restful import Resource, reqparse, request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token
from operations.Users import user_login


class UserLogin(Resource):

    def post(self):
        """
        To login the user and to generate 
        auth token
        """
        try:

            data = request.get_json()
            user = user_login.find_by_username(data['username'])
            if user and safe_str_cmp(user.password, data['password']):
                access_token = create_access_token(
                    identity=user.id, fresh=True)
                return {
                    'access_token': "Bearer " + access_token,
                }, 200
            return {"message": "Invalid Credentials!"}, 401
        except Exception as e:
            return {"message": str(e)}
