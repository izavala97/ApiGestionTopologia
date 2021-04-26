from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/inicio')
def home():
    return render_template('inicio.html')

@app.route('/info')
def about():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(debug=True)