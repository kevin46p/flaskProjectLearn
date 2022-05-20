# app.py
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    return app


app = create_app()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/520')
def love_520_lzy():
    return render_template("520lzy.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
