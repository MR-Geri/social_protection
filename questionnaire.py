from flask import request, render_template, Blueprint, redirect

blueprint = Blueprint(
    'questionnaire',
    __name__,
    template_folder='templates'
)


@blueprint.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        data = []
        select = request.form.get('1')[3:6]
        if select[2] != '0':
            income = int(select[0:2])
        else:
            income = int(select)
        number_people = int(request.form.get('2'))
        income /= number_people
        if income < 10:
            data.append(("Ваш доход ниже прожиточного минимума, Вам пологается государственная помощь.",
                            "http://www.kremlin.ru/acts/bank/14146"))
        select2 = request.form.get('3')
        if select2 == "да":
            data.append(("У Вас есть льготы",
                            "https://bankiros.ru/news/kakie-lgoty-i-posobia-dostupny-grazdanam-rf-vne-zavisimosti-ot-ih-dohoda-v-2021-godu-6882"))
        select3 = request.form.get('4') #субъективная оценка своего состояния гражданином
        if len(data) == 0:
            data.append("У Вас нет льгот")
        return render_template('survey_result.html', data=data)
    elif request.method == 'GET':
        return render_template('questionnaire.html')
