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
        self.app.add_url_rule("/", view_func=self.home())
    

    def run_server(self):
        self.server = threading.Thread(target=self.app.run, kwargs={"host": self.host, "port": self.port})
        self.server.start()
        return self.server


    def home(self):
        
        return render_template("hello.html")


if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, dest="config")

    args = parser.parse_args()

    config = config_par(args.config)

    server_host = config["HOST"]
    server_port = config["PORT"]

    server = Server(
        host=server_host,
        port=server_port
    )
    server.run_server()