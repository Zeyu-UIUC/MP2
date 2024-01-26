from flask import Flask, request, jsonify
import os
import socket
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip

@app.route('/', methods=['POST'])
def start_SC():
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return jsonify({'message': 'Process stress CPU.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')