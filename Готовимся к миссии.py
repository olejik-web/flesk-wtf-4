from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<name>')
def index(name):
    return render_template('base.html', title=name)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_prof.html', list=list)


@app.route('/auto_answer')
@app.route('/answer')
def answer():
    dictt = {
        'title': '������ �. �.',
        'surname': '��������',
        'name': '����',
        'education': '���� ��������',
        'profession': '������� ���������',
        'sex': 'male',
        'motivation': '������ ������ �������� �� �����!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', dict=dictt, title=dictt['title'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')