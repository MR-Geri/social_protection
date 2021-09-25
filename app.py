from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'social_protection_secret_key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pomosh')
def pomosh():
    return render_template('pomosh.html')


if __name__ == '__main__':
    app.run()
