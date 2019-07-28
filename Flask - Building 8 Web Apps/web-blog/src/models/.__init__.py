from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_method():
    retunr "Wubasbasb"

if __name__ == '__main__'
    app.run(port=4995)
