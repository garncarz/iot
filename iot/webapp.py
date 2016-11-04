from flask import (
    Flask, render_template, redirect, url_for, request,
)

from . import crawler, parser, gosms, settings


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', rec=crawler.get_last_record())


@app.route('/sms', methods=['POST'])
def sms():
    if not getattr(settings, 'CAN_SEND_SMS', False):
        return redirect(url_for('index'))

    phone = request.form['phone']
    if not phone:
        return redirect(url_for('index'))

    rec = crawler.get_last_record()
    msg = render_template('sms.txt', rec=rec)
    gosms.send(msg, recipients=phone)

    return render_template('sms_sent.html')
