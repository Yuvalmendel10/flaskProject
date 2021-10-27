from flask import Flask

from routes import indexRoute,createRoute,createLogIn

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app.register_blueprint(indexRoute)
app.register_blueprint(createRoute)
app.register_blueprint(createLogIn)


if __name__ == "__main__":
	app.run(debug=True)
