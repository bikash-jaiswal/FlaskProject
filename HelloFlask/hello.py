"""
Notes:
    - Create an application instance
     

"""
from flask import Flask
app = Flask(__name__)

'''
Notes: Routes and View Functons
Routes - link betn a URL and function that it handles it 
e.g app.route()


'''
@app.route("/")
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(port = 5000, debug=True)    