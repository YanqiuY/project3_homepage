from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def home():

    return render_template("index.html")


@app.route('/anyname')
def anyname():

    return render_template("anyname.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
