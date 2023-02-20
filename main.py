import os
from flask import Flask, render_template, request
from data import db_session
from data.databases import Schools, Otzivi
app = Flask(__name__)
db_session.global_init('db/schools_spb.db')
db_sess = db_session.create_session()


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main_page.html')


@app.route('/schools', methods=['GET', 'POST'])
def schools():
    schools_list = db_sess.query(Schools)
    return render_template('schools.html', schools=schools_list)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        search = request.values.get('search_all', default='')
        otziv = Otzivi()
        otziv.review = search
        print(search)
        db_sess.add(otziv)
        db_sess.commit()
    feedback_list = db_sess.query(Otzivi)
    return render_template('feedback.html', reviews=feedback_list)



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='192.168.0.115', port=port)