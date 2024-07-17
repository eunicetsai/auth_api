from flask import Flask, jsonify, request, render_template
# from flask_swagger_ui import get_swaggerui_blueprint
from swagger_ui import api_doc
from database import connect_db, create_user_table
from repositories.user import UserRepository
from services.user import UserService

app = Flask(__name__)

api_doc(app, config_path='swagger.yaml', url_prefix='/api/doc', title='User API doc')

def create_user_service():
  conn = connect_db()
  create_user_table(conn)
  user_repository = UserRepository(conn)  
  return UserService(user_repository) 

user_service = create_user_service()


@app.route('/api/user/verify', methods=['POST'])
def verify_user():
    try:
        # Retrieve username and password from request body
        username = request.json['username']
        password = request.json['password']

        # Validate required fields
        if not username or not password:
            return jsonify({"success": False, "reason": 'Missing required fields'}), 400

        user, msg = user_service.verify_user(username, password)
        if not user:
            return jsonify({"success": False, "reason": msg}), 400
        
        return jsonify({"success": bool(user), "reason": None}), 200            

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'Internal server error'}), 500
    

@app.route('/api/user/register', methods=['POST'])
def create_user():
    # Validate and handle potential errors in the request data
    try:
        username = request.json['username']
        password = request.json['password']
    except KeyError:
        return jsonify({"success": False, "reason": "Missing required fields: username or password"}), 400

    # Call UserService to create the user
    success, message = user_service.create_user(username, password)
 
    if success:
        return jsonify({"success": bool(success)}), 201
    else:
        return jsonify({"success": bool(success), "reason": message}), 400
    

if __name__ == '__main__':
    app.run(debug=True)