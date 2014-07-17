import flask
import settings

# Views
from main import Main
from login import Login
from cats import Cats
from dogs import Dogs  
from books import Books  

app = flask.Flask(__name__)
app.secret_key = settings.secret_key


# Routes
app.add_url_rule('/',
                 view_func=Login.as_view('login'),
                 methods=['GET', 'POST'])
app.add_url_rule('/cats/',
                 view_func=Cats.as_view('cats'),
                 methods=['GET', 'POST'])
app.add_url_rule('/dogs/',
                 view_func=Dogs.as_view('dogs'),
                 methods=['GET', 'POST'])
app.add_url_rule('/books/',
                 view_func=Books.as_view('books'),
                 methods=['GET', 'POST'])

app.debug = True
app.run()