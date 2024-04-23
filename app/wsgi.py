from flask import Flask 
import socket

app=Flask(__name__)

@app.route('/home')
def home():
    return f"hello from {socket.gethostname()}!"




if __name__ == '__main__':
    app.run(debug=True)