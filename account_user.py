from flask import request, render_template, current_app, Blueprint, redirect
from flask_login import login_user, login_required, current_user, logout_user, LoginManager
from database.utils import get_base, get_user_by_login

blueprint = Blueprint(
    'account_user',
    __name__,
    template_folder='templates'
)
login_manager = LoginManager()


@blueprint.route('/user')
def get_user():
    return 'Тест пройден'


@login_manager.user_loader
def load_user(user_id):
    with get_base() as base:
        return base.execute("""SELECT * FROM Users WHERE id = ?;""", (user_id, )).fetchall()[0]


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = get_user_by_login(request.form['login'])
        if user:
            login_user(user, remember=request.form.get('check', False))
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль")
    return render_template('login.html')


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")
