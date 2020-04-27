from flask import Flask
from flask_restful import Api
from resources.sparepart import Spareparts

app = Flask(__name__)
app.secret_key = 'rexwar'
api = Api(app)

api.add_resource(Spareparts, '/spareparts')

if __name__ == '__main__':
    app.run(port=443, debug=True)
