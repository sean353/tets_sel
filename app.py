from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# עמוד הבית
@app.route('/home')
def home():
    return '<h1>Welcome to the Home Page</h1>'

# עמוד לוגין
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # בדיקת שם משתמש וסיסמה
        if username == 'admin' and password == '12345':
            return redirect(url_for('home'))
        else:
            return 'Invalid Credentials. Please try again.'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
