from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/login')
def login_function():
    return 'This is a login page'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
