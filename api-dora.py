from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class FlaskDora(Resource):
    def get(self):
        return {'hello': 'doraemon'}

api.add_resource(FlaskDora, '/')

if __name__ == '__main__':
    app.run(debug=True)
