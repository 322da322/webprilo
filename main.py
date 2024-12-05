from flask import Flask, render_template
from flask import request # requests - для принятие данных(вроде бы)
import argparse
from utils import config_par
import threading





class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port


        self.app = Flask(__name__)

        self.app.add_url_rule("/shutdown", view_func=self.shutdown)
        self.app.add_url_rule("/", view_func=self.home, methods=["GET", "POST"])
        self.app.add_url_rule("/404", view_func=self.gifs)
    

    def run_server(self):
        self.app.run(debug=True)
        #self.server = threading.Thread(target=self.app.run, kwargs={"host": self.host, "port": self.port})
        print(self.host, self.port)
        #self.server.start()
        #return self.server




    def shutdown_server(self):
        request.get(f"http://{self.host}:{self.port}/shutdown")

    def shutdown(self):
        terminate_func = request.environ.get('werkzeuq.server.shutdown')
        if terminate_func:
            terminate_func()



    def home(self):
        output = None
        if request.method == "POST":
            user_input = request.form.get("user_input")  # Получаем данные из формы
            output = user_input  # Обрабатываем данные
            
        return render_template("file_input.html", output=output)
    

    def gifs(self):
        return render_template("test.html")
    




if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, dest="config")

    args = parser.parse_args()

    config = config_par("config.txt")

    server_host = config["HOST"]
    server_port = int(config["PORT"])

    server = Server(
        host=server_host,
        port=server_port
    )
    server.run_server()