from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import TinyDBDataAccess

app = Flask(__name__)
api = Api(app)

CORS(app)


@app.route("/hello")

def hello():
    return jsonify({'text':'Hello World!'})

class BooksTest(Resource):
    def get(self):
        aNewBook={'title':"hampster ball", 'upc':"28405108",'all_pages':239,'current_page':19,'notes':""}
        book2={'title':"Barbabany", 'upc':"0914809",'all_pages':7892,'current_page':223,'notes':"You wouldn't even believe...."}
        #return {'books': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]}
        return [aNewBook,book2] 

class Potato(Resource):
    def get(self):
        return 'a potato'

class Books(Resource):
    def get(self,userid):
        conn = TinyDBDataAccess.Connection()
        print("userID:"+userid)
        booksList = conn.getBooks(userid)
        print(booksList)
        return booksList


api.add_resource(Books, '/bookable/<userid>/') # Route_1
api.add_resource(Potato, '/potato')


if __name__ == '__main__':
     app.run(port=5002)