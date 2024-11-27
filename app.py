from flask import Flask, render_template

app = Flask(__name__)


def get_sum(x, y):
  return 'This is a function!'

@app.route("/")
def index():
  return render_template('index.html',
                         get_sum=get_sum)

