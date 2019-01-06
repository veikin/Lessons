from flask import Flask

app = Flask(__name__)


@app.route('/hello/<s1>')
def home(s1):
    return 'value: ' + s1


@app.route('/s1/<s2>')
def home2(s2):
    return 'value: ' + s2


if __name__ == "__main__":
    app.run()
