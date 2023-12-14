from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if (username == 'user1' and password == 'password1') or \
           (username == 'user2' and password == 'password2'):
            return redirect(url_for('home'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    return 'Logged in successfully.'

if __name__ == '__main__':
    app.run(debug=True)
