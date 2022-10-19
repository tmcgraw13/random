from back import random_int_generator
from mygame.tictactoe import start_turn
from flask import Flask, Response, jsonify
from flask_cors import CORS
from flask import request
from env import MyCurrentEnv

# instantiate the app
application = Flask(__name__)

# enable CORS
CORS(application, resources={r'/*': {'origins': '*'}})

# sanity check route
@application.route('/', methods=['GET'])
def get_random_str():
    return "URL works"

@application.route('/ping', methods=['GET'])
def get_random_int():
    return str(random_int_generator())

@application.route('/tictactoe', methods=['GET'])
def get_tictactoe_input():
    arrays = 3 
    board = [[''] * 3 for i in range(arrays)]
    spot = [1,1]
    return str(start_turn(spot,board))

@application.route('/test', methods=['POST'])
def post_tictactoe_input():
    b = request.json['board']
    return jsonify(start_turn(b))

if __name__ == '__main__':
    application.run(port=MyCurrentEnv.port)
