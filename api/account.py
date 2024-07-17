# from sqlite3 import DatabaseError
# from flask import jsonify
# from flask_restful import Resource, reqparse
# from services.user import UserService


# class CreateAccount(Resource):
#   parser = reqparse.RequestParser()
#   parser.add_argument('username', type=str, required=True, help="Username for the account")
#   parser.add_argument('password', type=str, required=True, help="Password for the account")

#   def __init__(self):
#     self.user_service = UserService()  # Inject the user service

#   def post(self):
#     try:
#       data = self.parser.parse_args()
#       username = data['username']
#       password = data['password']
#       self.user_service.create_user(username, password)
#       # Create and return the successful response model (replace with yours)
#       response = {"success": True}
#       return jsonify(response)
#     except DatabaseError as e:
#       return jsonify({"success": False, "reason": "Database error occurred"}), 500
#     except ValueError as e:  # Consider specific validation errors here
#       return jsonify({"success": False, "reason": str(e)}), 400  # Adjust status code if needed
#     except Exception as e:  # Catch other unexpected errors
#       return jsonify({"success": False, "reason": "An unexpected error occurred"}), 500


