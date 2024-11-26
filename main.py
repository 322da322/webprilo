from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello.html")
    print(123123123)


@app.route("/reg_run")
def index():
    a = request.form['name']
    print(a)



if __name__ == '__main__':
    app.run(debug=True)