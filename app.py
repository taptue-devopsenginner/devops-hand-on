from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def home():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return render_template('index.html', current_time=current_time)

@app.route('/api/time')
def api_time():
    return {'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
