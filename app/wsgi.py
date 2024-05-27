from flask import Flask 
import socket
from consistent_hashmap import ConsistentHashMap

app=Flask(__name__)

consistent_hashmap = ConsistentHashMap(512)

servers = ['server1', 'server2', 'server3']
for server in servers:

    consistent_hashmap.add_server(server)

@app.route('/home')
def home():
    return f"hello from {socket.gethostname()}!"




if __name__ == '__main__':
    app.run(debug=True)