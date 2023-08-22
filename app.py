from flask import Flask, render_template
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
import os

app = Flask(__name__)

# Configure JWT settings
app.config['JWT_SECRET_KEY'] = 'supersecretkey'
jwt = JWTManager(app)

# Define a route to serve index.html
@app.route('/')
def index():
    return render_template('index.html')

# Define a protected route that requires JWT authentication
@app.route('/protected')
@jwt_required()
def protected():
    return render_template('protected.html', username=get_jwt_identity())

if __name__ == '__main__':
    app.run()
