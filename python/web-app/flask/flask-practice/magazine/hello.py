from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html')


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        '127.0.0.1', 9090, app,
        use_debugger=True, use_reloader=True, processes=2,
    )
