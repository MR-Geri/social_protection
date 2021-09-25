import account_user
from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'social_protection_secret_key'
account_user.login_manager.init_app(app)
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
