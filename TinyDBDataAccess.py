from cgitb import text
from venv import create
from tinydb import TinyDB,Query

class Connection:
    db : any

    def __init__(self):
        self.db = TinyDB('~/dev/inventory-manager-back/tdb/db.json', create_dirs=True)

    def getBooks(self,userID: text):
        bookSearch = Query()
        books = self.db.search((bookSearch['type'] == 'book') & (bookSearch['user'] == int(userID)))
        #books = self.db.search(bookSearch['user'] == int(userID))
        #books = self.db.all()
        return books

    def putBook(self, userID, data):
        self.db.insert({'user': userID, 'book': data, 'type':'book', 'borrower':'','owner':userID})

    def getMovies(self, userID: text):
        movieSearch = Query()
        movies = self.db.search((movieSearch['type'] == 'movie') & (movieSearch['user'] == int(userID)))
        return movies

    def putMovies(self, userID, data):
        self.db.insert({'user':userID, 'movie': data, 'type':'movie', 'borrower':'','owner':userID})

    def getAlcohol(self, userID: text):
        alcoholSearch = Query()
        alcohol = self.db.search((alcoholSearch['type'] == 'alcohol') & (alcoholSearch['user'] == int(userID)))
        return alcohol
    
    def putAlcohol(self, userID, data):
        self.db.insert({'user':userID, 'alcohol':data, 'type':'alcohol', 'borrower':'', 'owner':userID})

if __name__ == '__main__':
    starter = Connection()
    #starter.putBook(1,{'title':"Barbabany", 'upc':"0914809",'all_pages':7892,'current_page':223,'notes':"You wouldn't even believe...."})
    print(starter.getBooks(1))