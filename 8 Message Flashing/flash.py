# API 확인
# https://flask.palletsprojects.com/en/2.0.x/api/#message-flashing
# https://pythonise.com/series/learning-flask/flask-message-flashing

from flask import *
app = Flask(__name__)
app.secret_key = 'random string'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
           request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('성공적으로 로그인되었습니다!')
            return redirect(url_for('index'))

    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)