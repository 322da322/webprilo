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
        self.app.add_url_rule("/", view_func=self.home)
        self.app.add_url_rule("/home", view_func=self.home)
    

    def run_server(self):
        self.server = threading.Thread(target=self.app.run, kwargs={"host": self.host, "port": self.port})
        print(self.host, self.port)
        self.server.start()
        return self.server




    def shutdown_server(self):
        request.get(f"http://{self.host}:{self.port}/shutdown")

    def shutdown(self):
        terminate_func = request.environ.get('werkzeuq.server.shutdown')
        if terminate_func:
            terminate_func()



    def home(self):
        
        return render_template("hello.html",r="Russia")


if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, dest="config")

    args = parser.parse_args()

    config = config_par("C:\\Users\\alexh\\Desktop\\web\\config.txt")

    server_host = config["HOST"]
    server_port = int(config["PORT"])

    server = Server(
        host=server_host,
        port=server_port
    )
    server.run_server()