from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/woo')
def nature_call():
    return "woooooooooo"

if __name__ == '__main__':
    app.run()