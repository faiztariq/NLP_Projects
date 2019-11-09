from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return '<h2>Hello, Flask!</h2>'

@app.route('/hello')
@app.route('/hello/<name>')
def hello_global(name=None):
    return render_template('hello.html', name=name)

@app.route('/integer/<int:num>')
def integer_num(num):
    return '<h2>You entered : %d</h2>' %num

if __name__ == '__main__':
    app.run(debug=True)