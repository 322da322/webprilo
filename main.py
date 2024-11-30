from flask import Flask, render_template
from flask import request # requests - для принятие данных(вроде бы)
import time





class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port


        self.app = Flask(__name__)
        self.app.add_url_rule("/", view_func=self.home())
    



    def home(self):
        return "Хуй"


if __name__== '__main__':
    app.run(debug=True)