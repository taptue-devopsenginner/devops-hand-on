from flask import Flask, render_template, request, redirect, url_for
import time

app = Flask(__name__)

@app.route('/')
def home():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return render_template('index.html', current_time=current_time)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        if username != 'admin' or password != 'pa55word':
            error = 'Invalid username or password'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/api/time')
def api_time():
    return {'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
