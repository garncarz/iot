from flask import Flask, render_template

from . import crawler, parser


app = Flask(__name__)


@app.route('/')
def index():
    batch = crawler.get()
    rec = parser.parse(batch['records'][-1])

    return render_template('index.html', rec=rec)
