from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
database = SQLAlchemy(app)
id_final = 0


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
                       value_1=0, answer_2='45 - 54 года', value_2=2, answer_3='55 - 64 года', value_3=3,
                       answer_4='От 65 лет', value_4=4, value=None)
database.session.add(question_1)
length_list += 1

question_2 = Questions(question='Какой индекс массы вашего тела?',
                       text_of_question='Чтобы найти индекс массы, нужно разделить ваш вес на рост.', answer_1='До 25',
                       value_1=0, answer_2='25 - 30', value_2=1, answer_3='От 30', value_3=2, answer_4='', value_4=-1,
                       value=None)
database.session.add(question_2)
length_list += 1

question_3 = Questions(question='Имеются ли у вас аутоиммунные болезни?',
                       text_of_question='Гломерулонефрит, аутоиммунный тиреоидит, гепатит, волчанка и пр.',
                       answer_1='Да', value_1=1, answer_2='', value_2=-1, answer_3='Нет', value_3=0, answer_4='',
                       value_4=-1, value=None)
database.session.add(question_3)
length_list += 1

question_4 = Questions(question='Больны ли диабетом ваши родственники?',
                       text_of_question='Как правило, сахарный диабет в несколько раз чаще встречается у родственников больных сахарным диабетом.',
                       answer_1='Да, оба родителя', value_1=3, answer_2='Да, один родитель', value_2=2,
                       answer_3='Да, брат или сестра', value_3=1, answer_4='Нет', value_4=0, value=None)
database.session.add(question_4)
length_list += 1

question_5 = Questions(question='Есть ли у вас вирусные инфекции?',
                       text_of_question='Краснуха, вирусный паротит (свинка), ветряная оспа, вирусный гепатит и т.п.',
                       answer_1='Да', value_1=1, answer_2='', value_2=-1, answer_3='Нет', value_3=0, answer_4='',
                       value_4=-1, value=None)
database.session.add(question_5)
length_list += 1

question_6 = Questions(question='Испытываете ли вы...',
                       text_of_question='учащенные мочеиспускания, повышенную утомляемость, сонливость, тошноту, частое дыхание, зуд кожи?',
                       answer_1='Да, некоторые', value_1=1, answer_2='Да, все', value_2=2, answer_3='Нет', value_3=0,
                       answer_4='', value_4=-1, value=None)
database.session.add(question_6)
length_list += 1

database.session.commit()


@app.route('/')
def hello():
    questions = Questions.query.all()
    return render_template('hello.html', questions=questions)


@app.route('/question/<int:id>', methods=["POST", "GET"])
def question(id):
    questions = Questions.query.get(id)
    questions_database = Questions.query.all()

    if request.method == "POST":
        answer = request.form.get('petal_radio')
        if answer is not None and answer != '-1':
            Questions.query.get(id).value = answer
            database.session.commit()
        else:
            return make_response('Выберите ответ!')

    return render_template('question.html', questions=questions, questions_database=questions_database)


@app.route('/question/result/', methods=["POST", "GET"])
def result():
    if request.method == "POST":
        answer = request.form.get('petal_radio')
        if answer is not None and answer != '-1':
            Questions.query.get(id_final + 1).value = answer
            database.session.commit()
        else:
            return make_response('Выберите ответ!')

    final_percentage = 0
    for cycle_id in range(1, length_list + 1):
        final_percentage += Questions.query.get(cycle_id).value

    if final_percentage <= 13 / 3 * 1:
        return render_template('result_good.html', persentage=final_percentage)
    elif final_percentage <= 13 / 3 * 2:
        return render_template('result_ok.html', persentage=final_percentage)
    else:
        return render_template('result_bad.html', persentage=final_percentage)


if __name__ == "__main__":
    app.run(debug=True)
