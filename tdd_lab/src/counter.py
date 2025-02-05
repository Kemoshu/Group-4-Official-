"""Counter API Implementation"""
from flask import Flask, jsonify
from . import status

app = Flask(__name__)

COUNTERS = {}

def counter_exists(name):
  """Check if counter exists"""
  return name in COUNTERS

@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
  """Create a counter"""
  if counter_exists(name):
      return jsonify({"error": f"Counter {name} already exists"}), status.HTTP_409_CONFLICT
  COUNTERS[name] = 0
  return jsonify({name: COUNTERS[name]}), status.HTTP_201_CREATED

# Function #8: Prevent deleting non-existent counter
@app.route('/counters/<name>', methods=['DELETE'])
def deleting_nonexistent_counter(name):
   '''Prevent deleting non-existent counter'''
   if not counter_exists(name):
      return jsonify(name), status.HTTP_409_CONFLICT
   else:
      return jsonify(name), status.HTTP_200_OK

# Function #10: List counters
@app.route('/counters', methods=['GET'])
def list_counters():
    """List all counters"""
    # get just the counter names
    counterNames = list(COUNTERS.keys())
    return jsonify(counterNames), status.HTTP_200_OK 
