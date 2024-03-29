from re import U
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import TinyDBDataAccess

app = Flask(__name__)
api = Api(app)

CORS(app)


@app.route("/hello")

class BooksTest(Resource):
    def get(self):
        aNewBook={'title':"hampster ball", 'upc':"28405108",'all_pages':239,'current_page':19,'notes':""}
        book2={'title':"Barbabany", 'upc':"0914809",'all_pages':7892,'current_page':223,'notes':"You wouldn't even believe...."}
        return [aNewBook,book2] 

class Potato(Resource):
    def get(self):
        return 'a potato'

class Books(Resource):
    def get(self,userid):
        conn = TinyDBDataAccess.Connection()
        booksList = conn.getBooks(userid)
        return booksList
    
    def post(self,userid):
        bookData = self.parseParams(request)
        conn = TinyDBDataAccess.Connection()
        conn.putBook(userid,bookData)
        
    def put(self,userid,params):
        pass

    def parseParams(self, request):
        title = request.args.get('title')
        upc = request.args.get('upc')
        all_pages = request.args.get('all_pages')
        current_page = request.args.get('current_page')
        notes = request.args.get('notes')
        author = request.args.get('author')
        parsedData = {'title':title,'upc':upc,'all_pages':all_pages,'current_page':current_page,'notes':notes,'author':author}
        return parsedData
    
    def delete(self,userid):
        bookid=request.args.get('doc_id')
        conn = TinyDBDataAccess.Connection()
        conn.removeBook(userid, bookid)


class Alcohol(Resource):
    def get(self,userid):
        conn = TinyDBDataAccess.Connection()
        print("Alcohol - Userid: " + userid)
        alcoholList = conn.getAlcohol(userid)
        print(alcoholList)
        return alcoholList

    def post(self,userid,alcoholdata):
        conn = TinyDBDataAccess.Connection()
        conn.putAlcohol(userid,alcoholdata)

class Movies(Resource):
    def get(self,userid):
        conn = TinyDBDataAccess.Connection()
        print("Movie - userid: " + userid)
        movieList = conn.getMovies(userid)
        print(movieList)
        return movieList
    
    def post(self,userid,moviedata):
        conn = TinyDBDataAccess.Connection()
        conn.putMovies(userid, moviedata)

api.add_resource(Books, '/bookable/<userid>/') # Route_1
api.add_resource(Movies, '/movies/<userid>/') # Route_2
api.add_resource(Alcohol, '/alcohol/<userid>/') #Route_3
api.add_resource(Potato, '/potato')


if __name__ == '__main__':
     app.run(port=5002)