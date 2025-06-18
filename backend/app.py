from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.devices import device_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Register the device routes
app.register_blueprint(device_routes)

@app.route('/')
def index():
    return "Welcome to the My LAN Dashboard API!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)