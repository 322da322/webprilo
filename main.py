from flask import Flask, render_template
from flask import request # requests - для принятие данных(вроде бы)
from adduser import DB
from utils import config_par
import threading
import argparse
db = DB()


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







#<input type="email" name="email" placeholder="Email" required=""> file_input.html
    def home(self):
        print(123)
        if request.method == "POST":
            print(1111111111111111111)
            with open('C:\\Users\\alexh\\Desktop\\web\\filess\\numers_user.text', 'r+', encoding='utf-8') as f:
                user_id = f.read()
                f.close()
            with open('C:\\Users\\alexh\\Desktop\\web\\filess\\numers_user.text', 'w+', encoding='utf-8') as f:
                f.write(str(int(user_id) + 1))
                f.close()
            user_name = request.form.get("username")  # Получаем данные из формы
            user_passsword = request.form.get("password") 
            print(user_name, user_passsword)
            db.add_user(id= int(user_id), username= user_name, password= user_passsword)
        return render_template("file_input.html")
    

    def gifs(self):
        return render_template("test.html")
    




if __name__== '__main__':
    

    server = Server(
        host=None,
        port=None
    )
    server.run_server()