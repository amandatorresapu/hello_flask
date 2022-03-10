from distutils.log import debug
from operator import truediv
from flask import flask #import flask and create application
app = Flask(__name__)


@app.route("/")
def hello_world();
    return "hello world!"

if __name__ == "__main__"
    app.run(debug=true)