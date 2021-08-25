from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def Namaskara(name):
    return 'Namaskara ' + name

if __name__ == '__main__':
    app.run()