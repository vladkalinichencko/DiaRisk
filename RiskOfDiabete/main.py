from flask import *
from flask_sqlalchemy import SQLAlchemy

file = open('doc.txt', 'w')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
database = SQLAlchemy(app)
id_final = 0
max_points = 0
table = []


class Questions(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    question = database.Column(database.Text, nullable=True)
    text_of_question = database.Column(database.Text, nullable=True)
    answer_1 = database.Column(database.Text, nullable=True)
    value_1 = database.Column(database.Integer, nullable=True)
    answer_2 = database.Column(database.Text, nullable=True)
    value_2 = database.Column(database.Integer, nullable=True)
    answer_3 = database.Column(database.Text, nullable=True)
    value_3 = database.Column(database.Integer, nullable=True)
    answer_4 = database.Column(database.Text, nullable=True)
    value_4 = database.Column(database.Integer, nullable=True)
    value = database.Column(database.Integer, nullable=True)

    def __repr__(self):
        return '<Questions %r>' % self.id


length_list = 0
Questions.query.delete()

question_1 = Questions(question='Каков ваш возраст?', text_of_question='Каков ваш возраст?', answer_1='До 45 лет',
                       value_1='0|До 45 лет', answer_2='45 - 54 года', value_2='2|45 - 54 года', answer_3='55 - 64 года', value_3='3|55 - 64 года',
                       answer_4='От 65 лет', value_4='4|От 65 лет', value=None)
database.session.add(question_1)
length_list += 1

question_2 = Questions(question='Каков индекс массы вашего тела? (Наведите на круг для подробностей)',
                       text_of_question='Чтобы найти индекс массы, нужно разделить ваш вес (в килограммах) на рост (в метрах), возведённый в квадрат.', answer_1='До 25',
                       value_1='0|До 25 кг/м^2', answer_2='25 - 30', value_2='1|25 - 30 кг/м^2', answer_3='От 30', value_3='2|От 30 кг/м^2', answer_4='', value_4='-1| ',
                       value=None)
database.session.add(question_2)
length_list += 1

question_3 = Questions(question='Имеются ли у вас аутоиммунные болезни? (Наведите на круг для подробностей)',
                       text_of_question='Гломерулонефрит, аутоиммунный тиреоидит, гепатит, волчанка и пр.',
                       answer_1='Да', value_1='1|Да', answer_2='', value_2='-1| ', answer_3='Нет', value_3='0|Нет', answer_4='',
                       value_4='-1| ', value=None)
database.session.add(question_3)
length_list += 1

question_4 = Questions(question='Больны ли диабетом ваши родственники? (Наведите на круг для подробностей)',
                       text_of_question='Как правило, сахарный диабет в несколько раз чаще встречается у родственников больных сахарным диабетом.',
                       answer_1='Да, оба родителя', value_1='3|Да, оба родителя', answer_2='Да, один родитель', value_2='2|Да, один родитель',
                       answer_3='Да, брат или сестра', value_3='1|Да, брат или сестра', answer_4='Нет', value_4='0| ', value=None)
database.session.add(question_4)
length_list += 1

question_5 = Questions(question='Есть ли у вас вирусные инфекции? (Наведите на круг для подробностей)',
                       text_of_question='Инфекции, которые разрушают клетки поджелудочной железы, вырабатывающие инсулин: краснуха, вирусный паротит (свинка), ветряная оспа, вирусный гепатит и т.п.',
                       answer_1='Да', value_1='1|Да', answer_2='', value_2='-1| ', answer_3='Нет', value_3='0|Нет', answer_4='',
                       value_4='-1| ', value=None)
database.session.add(question_5)
length_list += 1

question_6 = Questions(question='Испытываете ли вы... (Наведите на круг для подробностей)',
                       text_of_question='учащенные мочеиспускания, повышенную утомляемость, сонливость, тошноту, частое дыхание, зуд кожи?',
                       answer_1='Да, некоторые', value_1='1|Да, некоторые', answer_2='Да, все', value_2='2|Да, все', answer_3='Нет', value_3='0|Нет',
                       answer_4='', value_4='-1| ', value=None)
database.session.add(question_6)
length_list += 1

question_7 = Questions(question='Ведёте ли вы здоровый образ жизни? (Наведите на круг для подробностей)',
                       text_of_question='Правильно ли вы питаетесь и занимаетесь ли вы спортом?',
                       answer_1='Да, частично', value_1='1|Да, частично', answer_2='Да', value_2='2|Да', answer_3='Нет', value_3='0|Нет',
                       answer_4='', value_4='-1| ', value=None)
database.session.add(question_7)
length_list += 1

question_8 = Questions(question='Был ли у вас диабет во время беременности? (Наведите на круг для подробностей)',
                       text_of_question='Если у вас был диабет во время беременности или у Вас родился ребенок весом более 4 кг.',
                       answer_1='Да', value_1='1|Да', answer_2='', value_2='-1| ', answer_3='Нет', value_3='0|Нет',
                       answer_4='', value_4='-1| ', value=None)
database.session.add(question_8)
length_list += 1

question_9 = Questions(question='Есть ли вас гипертензия? (Наведите на круг для подробностей)',
                       text_of_question='Если у Вас высокое артериальное давление (т.е. выше 140/90 мм рт. ст.), у вас повышенный риск появления диабета.',
                       answer_1='Да', value_1='1|Да', answer_2='', value_2='-1| ', answer_3='Нет', value_3='0|Нет',
                       answer_4='', value_4='-1| ', value=None)
database.session.add(question_9)
length_list += 1

question_10 = Questions(question='Есть ли у вас синдром поликистоза яичников? (Наведите на круг для подробностей)',
                       text_of_question='СПКЯ возникает при нарушении гормонального баланса у женщин и также связан с повышенным риском заболевания диабетом.',
                       answer_1='Да', value_1='1|Да', answer_2='', value_2='-1| ', answer_3='Нет', value_3='0|Нет',
                       answer_4='', value_4='-1| ', value=None)
database.session.add(question_10)
length_list += 1

question_11 = Questions(question='Обнаруживали ли у Вас когда-либо уровень сахара в крови выше нормы? (Наведите на круг для подробностей)',
                       text_of_question='Во время диспансеризации, проф. осмотра, во время болезни или беременности.',
                       answer_1='Да', value_1='1|Да', answer_2='', value_2='-1| ', answer_3='Нет', value_3='0|Нет',
                       answer_4='', value_4='-1| ', value=None)
database.session.add(question_11)
length_list += 1

max_points = 19
database.session.commit()

table.append(['Возраст: '])
table.append(['Индекс массы: '])
table.append(['Аутоиммунные болезни: '])
table.append(['Генетическая предрасположенность: '])
table.append(['Вирусные инфекции: '])
table.append(['Симптомы: '])
table.append(['Здоровый образ жизни: '])
table.append(['Диабет во время беременности: '])
table.append(['Гипертензия: '])
table.append(['СПКЯ: '])
table.append(['Уровень сахара выше нормы: '])


@app.route('/')
def hello():
    questions = Questions.query.all()
    return render_template('hello.html', questions=questions)


@app.route('/report')
def show_report():
    return send_file('doc.txt', as_attachment=True)


@app.route('/question/<int:id>', methods=["POST", "GET"])
def question(id):
    questions = Questions.query.get(id)
    questions_database = Questions.query.all()

    if request.method == "POST":
        answer = request.form.get('petal_radio')
        answer = answer.split('|')
        if answer is not None and answer[0] != '-1':
            Questions.query.get(id).value = int(answer[0])
            database.session.commit()

            table[id - 1].append(answer[1])
        else:
            return make_response('Выберите ответ!')

    return render_template('question.html', questions=questions, questions_database=questions_database)


@app.route('/question/result/', methods=["POST", "GET"])
def result():
    if request.method == "POST":
        answer = request.form.get('petal_radio')
        answer = answer.split('|')
        if answer is not None and answer[0] != '-1':
            Questions.query.get(id_final + 1).value = int(answer[0])
            database.session.commit()

            table[id_final].append(answer[1])
        else:
            return make_response('Выберите ответ!')

    for row in table:
        for item in row:
            file.write(item)
        file.write('\n')

    file.close()

    final_percentage = 0
    for cycle_id in range(1, length_list + 1):
        final_percentage += Questions.query.get(cycle_id).value

    if final_percentage <= max_points / 3 * 1:
        return render_template('result_good.html', persentage=final_percentage)
    elif final_percentage <= max_points / 3 * 2:
        return render_template('result_ok.html', persentage=final_percentage)
    else:
        return render_template('result_bad.html', persentage=final_percentage)


if __name__ == "__main__":
    app.run(debug=False)
