from flask import Flask, render_template
from random import randint
app = Flask(__name__)

@app.route('/')
def realtime():
    return render_template('realtime.html')

@app.route('/arousallevel/')
def arousal_level():
    return str(randint(0, 100))

if __name__ == '__main__':
    app.run(debug=True)
