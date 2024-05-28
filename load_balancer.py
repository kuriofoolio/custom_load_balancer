from flask import Flask, request, jsonify
import random
from consistent_hashing import ConsistentHashMap

app = Flask(__name__)
N = 3
hash_map = ConsistentHashMap(num_slots=100)
servers = ["Server 1", "Server 2", "Server 3"]

# Add initial servers
for server in servers:
    hash_map.add_server(server)

def generate_random_hostname():
    return "Server-" + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))

@app.route('/rep', methods=['GET'])
def get_replicas():
    response = {
        "message": {
            "N": len(servers),
            "replicas": servers
        },
        "status": "successful"
    }
    return jsonify(response), 200

@app.route('/add', methods=['POST'])
def add_replicas():
    data = request.get_json()
    new_instances = data.get('n')
    hostnames = data.get('hostnames', [])
    
    if len(hostnames) > new_instances:
        response = {
            "message": "<Error> Length of hostname list is more than newly added instances",
            "status": "failure"
        }
        return jsonify(response), 400
    
    new_servers = []
    for i in range(new_instances):
        if i < len(hostnames):
            new_server = hostnames[i]
        else:
            new_server = generate_random_hostname()
        new_servers.append(new_server)
        hash_map.add_server(new_server)
    
    servers.extend(new_servers)
    
    response = {
        "message": {
            "N": len(servers),
            "replicas": servers
        },
        "status": "successful"
    }
    return jsonify(response), 200

@app.route('/rm', methods=['DELETE'])
def remove_replicas():
    data = request.get_json()
    instances_to_remove = data.get('n')
    hostnames = data.get('hostnames', [])
    
    if len(hostnames) > instances_to_remove:
        response = {
            "message": "<Error> Length of hostname list is more than removable instances",
            "status": "failure"
        }
        return jsonify(response), 400
    
    if instances_to_remove > len(servers):
        instances_to_remove = len(servers)
    
    removable_servers = set(hostnames)
    while len(removable_servers) < instances_to_remove:
        random_server = random.choice(servers)
        removable_servers.add(random_server)
    
    for server in removable_servers:
        hash_map.remove_server(server)
        servers.remove(server)
    
    response = {
        "message": {
            "N": len(servers),
            "replicas": servers
        },
        "status": "successful"
    }
    return jsonify(response), 200

@app.route('/<path:path>', methods=['GET'])
def route_request(path):
    if path != "home":
        response = {
            "message": f"<Error> '/{path}' endpoint does not exist in server replicas",
            "status": "failure"
        }
        return jsonify(response), 400
    
    # Simulate a request routing to one of the servers
    server = hash_map.get_server(path)
    response = {
        "message": f"Request routed to {server}",
        "status": "successful"
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
