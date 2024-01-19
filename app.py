from flask import Flask, render_template
from flask_socketio import SocketIO, send
from dotenv import load_dotenv
import os
# import request

load_dotenv()

app = Flask(__name__)
#De esta manera (con el secret key) no se subirá la clave a github
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)

@app.route('/')

def index():
    return render_template('index.html')

@socketio.on('message')

def handleMessage(msg):
    print("Message: ",msg)
    send(msg, broadcast = True)

    # clientIP = request.connection.remoteAddresss
    # print(clientIP)

if __name__ == "__main__":
    socketio.run(app, port=3000, debug=True) #Si añadimos al final host="0.0.0.0" y alguien pone nuestra IP en su navegador, será un chat entre los 2