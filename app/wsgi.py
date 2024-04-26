from flask import Flask , jsonify
import socket

app=Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    response_data = {'message': f'Hello from Server {socket.gethostname()}', 'status code':200}
    return jsonify(response_data)
    # return f"Hello from Server {socket.gethostname()}"

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    response_data = {'message': 'Server is up and running', 'status code':200}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)


    
