from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)  
# Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!' 

@app.route("/success") 
def sucess():
    return 'meow'

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    return "Hello, " + name


@app.route("/hello/<string:banana>/<int:num>")
def render(banana, num):
    return F"hello {banana * num} out"


if __name__=="__main__":   
    app.run(debug=True)    

