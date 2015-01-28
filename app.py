import random
from flask import Flask, render_template
#init repo
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():

    jerk_status = True

    if random.random() > 0.5:
        jerk_status = False
        
    return render_template('index.html', jerk_status=jerk_status)

if __name__ == '__main__':
    app.run()