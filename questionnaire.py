from flask import request, render_template, Blueprint, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy

blueprint = Blueprint(
    'questionnaire',
    __name__,
    template_folder='templates'
)

@blueprint.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        select = request.form.get('1')
        select1 = request.form.get('2')
        select2 = request.form.get('3')
        select3 = request.form.get('4')
        return("Прошел опрос? Молодец, возьми с полки пирожок)")
    elif request.method == 'GET':
        return render_template('questionnaire.html')
