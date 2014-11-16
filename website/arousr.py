from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
client = None
socketio = SocketIO(app)
currentArousalLevel = 0
trigger = False
timeInThisTrigger = 0

@app.route('/')
def realtime():
    return render_template('realtime.html')

@app.route('/getarousallevel/')
def arousal_level():
    return str(currentArousalLevel)

@app.route('/isaroused/')
def isaroused():
    global trigger
    if trigger:
        trigger = False
        return "True"
    else:
        return "False"

@app.route('/setarousallevel/<float:arousal>')
def set_arousal_level(arousal):
    global currentArousalLevel
    currentArousalLevel = arousal
    return "ok"

@app.route('/trigger')
def set_trigger():
    print "Got trigger"
    global trigger
    global timeInThisTrigger
    if not trigger and not timeInThisTrigger > 0:
        trigger = True
        timeInThisTrigger = 7
    if not trigger:
        timeInThisTrigger -= 1
    return "ok"

if __name__ == '__main__':
    app.run(debug=True)
