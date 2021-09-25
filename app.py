import account_user
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/base.sqlite'
db = SQLAlchemy(app)  # Важная для работы базы данных строка
from account_user import login_manager

login_manager.init_app(app)
app.register_blueprint(account_user.blueprint)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/info')
def info():
    return render_template('info.html')


if __name__ == '__main__':
    app.run()
