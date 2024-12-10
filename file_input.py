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

'''
.rainbow_bob {
            text-align: justify;
        }

<div class="rainbow_bob">
        {% if output %}
            <h2>Вы ввели: {{ output }}</h2>
            <h3>Ема ты крыса, на Саню быкуешь за спиной? Очкошник ты в лицо ему что он: {{output}}</h3>
            <h3>Я ожидал разного, что Саня патриот, пилот, программист, но никак не: {{output}}</h3>
        {% endif %}
'''
