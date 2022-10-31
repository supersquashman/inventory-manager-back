from flask import Flask, request
from flask_restful import Resource, Api
from fask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)

class Books(Resource):
    def get(self):
        return {'books': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

api.add_resource(Books, '/books') # Route_1

if __name__ == '__main__':
     app.run(port=5002)