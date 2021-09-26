from flask import request, render_template, Blueprint, redirect

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
        data = "Вам пологаются соц. выплаты"  # расчет льгот если они есть
        return render_template('survey_result.html', data=data)
    elif request.method == 'GET':
        return render_template('questionnaire.html')
