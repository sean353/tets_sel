from flask import Flask, request, redirect, url_for

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
            return "Login successful."
        else:
            return 'Invalid Credentials. Please try again.'

    # HTML של עמוד הלוגין
    login_page = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Page</title>
    </head>
    <body>
        <h2>Login Page</h2>
        <form action="/login" method="POST">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <br><br>
            <button type="submit">Login</button>
        </form>
    </body>
    <script>
     document.getElementById('loginForm').addEventListener('submit', function(event) {
            event.preventDefault();

            const username = document.getElementById("username").value;
            const password= document.getElementById("password").value;

            const messageDiv = document.getElementById('message');

            const valisUsername = "admin"
            const valisPassword = "12345"

            if (username == valisUsername && password == valisPassword){
                messageDiv.textContent = 'login succsessfull.';
                messageDiv.style.color = 'green';
            }else{
                messageDiv.textContent = 'Invalid username or password.';
                messageDiv.style.color = 'red';
            }


     })
</script>
    </html>
    '''
    return login_page

if __name__ == '__main__':
    app.run(debug=True)
