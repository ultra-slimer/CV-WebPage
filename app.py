from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/heyoo')
def testing():
    return render_template("hello.html", name="ASDA")
