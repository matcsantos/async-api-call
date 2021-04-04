
# Simulates a slow API.

from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/hash/<seed>')
def generate_hash(seed:str):
    
    time.sleep(1) # some processing time

    return jsonify({
        'seed':seed,
        'hash':hash(seed)
    })

if __name__ == '__main__':
    app.run('localhost')
