from flask import Flask, render_template
from random import randint
app = Flask(__name__)

@app.route('/')
def realtime():
    return render_template('realtime.html')

# aroused on a scale of 1 to 10
# 1 = green, 10 = red
@app.route('/arousallevel/')
def arousal_level():
    return str(randint(1, 10))

if __name__ == '__main__':
    app.run(debug=True)
