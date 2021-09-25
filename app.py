import account_user
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user

from database.utils import get_base

app = Flask(__name__)
app.config['SECRET_KEY'] = 'social_protection_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/base.sqlite'
db = SQLAlchemy(app)  # Важная для работы базы данных строка
from account_user import login_manager

login_manager.init_app(app)
app.register_blueprint(account_user.blueprint)


@app.route('/')
def index():
    return render_template('index.html', modal_info=False)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/info')
def info():
    if current_user.is_authenticated:
        """Численность безработных граждан по МО УР на 01.01.2021г."""
        poverty = {'titles': [], 'values': []}
        zarp = {'titles': [], 'reporting_month': [], 'period_from_beginning_reporting_year': [],
                'last_moth': [], 'last_year': [], 'beginning_reporting_period_previous_year': []}
        with get_base('database/base.sqlite') as base:
            for i in base.execute("""SELECT * FROM unemployed_citizens;""").fetchall():
                poverty['titles'].append(i[1].strip())
                poverty['values'].append(int(i[2]))
        with get_base('database/base.sqlite') as base:
            for i in base.execute("""SELECT * FROM zarpMO;""").fetchall():
                zarp['titles'].append(i[1])
                zarp['reporting_month'].append(i[2])
                zarp['period_from_beginning_reporting_year'].append(i[3])
                zarp['last_moth'].append(i[4])
                zarp['last_year'].append(i[5])
                zarp['beginning_reporting_period_previous_year'].append(i[6])
        return render_template('info.html', poverty=poverty, zarp=zarp)
    else:
        return redirect('/')


@app.route('/questionnaire')
def questionnaire():
    return render_template('questionnaire.html')


if __name__ == '__main__':
    app.run()
