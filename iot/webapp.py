from flask import Flask, render_template

from . import crawler, parser, gosms


app = Flask(__name__)


@app.route('/')
def index():
    batch = crawler.get()
    rec = parser.parse(batch['records'][-1])

    return render_template('index.html', rec=rec)


@app.route('/sms')
def sms():
    batch = crawler.get()
    rec = parser.parse(batch['records'][-1])

    msg = render_template('sms.txt', rec=rec)
    gosms.send(msg)

    return render_template('sms_sent.html')
