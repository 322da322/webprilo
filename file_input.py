from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = None
    if request.method == "POST":
        user_input = request.form.get("user_input")  # Получаем данные из формы
        output = user_input  # Обрабатываем данные
    return render_template("test.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
