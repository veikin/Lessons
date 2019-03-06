from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/products')
def products_list()


@app.route('/products/<int:priduct_id>')
def product_list(product_id)


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        '127.0.0.1', 9090, app,
        use_debugger=True, use_reloader=True, processes=2,
    )
