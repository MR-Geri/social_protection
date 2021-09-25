import account_user
import questionnaire
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'social_protection_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/base.sqlite'
db = SQLAlchemy(app)  # Важная для работы базы данных строка
from account_user import login_manager

login_manager.init_app(app)
app.register_blueprint(account_user.blueprint)
app.register_blueprint(questionnaire.blueprint)


@app.route('/')
def index():
    return render_template('index.html', modal_info=False)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/info')
def info():
    if current_user.is_authenticated:
        return render_template('info.html')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run()
