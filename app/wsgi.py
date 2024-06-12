from flask import Flask , jsonify
import socket
from consistent_hashmap import ConsistentHashMap

app=Flask(__name__)

consistent_hashmap = ConsistentHashMap(512)

servers = ['server1', 'server2', 'server3']
for server in servers:

    consistent_hashmap.add_server(server)

@app.route('/home')
def home():
    response_data = {'message': f'Hello from Server {socket.gethostname()}', 'status code':200}
    return jsonify(response_data)

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    response_data = {'message': f'Server {socket.gethostname()} is up and running', 'status code':200}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)