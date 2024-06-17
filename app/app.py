from flask import Flask, jsonify, request

app = Flask(__name__)

# Define routes for each replica
@app.route('/server1', methods=['GET'])
def replica1():
    return jsonify({'message': 'Response from server1'})

@app.route('/server2', methods=['GET'])
def replica2():
    return jsonify({'message': 'Response from server2'})

@app.route('/server3', methods=['GET'])
def replica3():
    return jsonify({'message': 'Response from server3'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)