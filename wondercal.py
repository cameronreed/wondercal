"""
    WonderCal
    ~~~~~~~~~~

    A wonderful calendar.

    :copyright: (c) 2014 by TimePickle Team

"""
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def landing_page():
    if request.method == 'POST':
        return redirect('/thanks')
    else:
        return render_template('index.html')


@app.route('/2')
def ab_landing_page():
    return render_template('index-b.html')


@app.route('/team')
def team_page():
    return render_template('our-team.html')


@app.route('/team2')
def ab_team_page():
    return render_template('our-team-b.html')


@app.route('/faq')
def faq_page():
    return render_template('faq.html')


@app.route('/faq2')
def ab_faq_page():
    return render_template('faq-b.html')


@app.route('/beta')
def beta_page():
    return render_template('beta.html')


@app.route('/thanks')
def email_confirm_page():
    return render_template('beta.html')


if __name__ == '__main__':
    app.run(debug=True)
