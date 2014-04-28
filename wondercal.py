"""
    WonderCal
    ~~~~~~~~~~

    A wonderful calendar.

    :copyright: (c) 2014 by TimePickle Team

"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('index.html')


@app.route('/2')
def ab_landing():
    return render_template('index-b.html')


if __name__ == '__main__':
    app.run(debug=True)
