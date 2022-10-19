from back import random_int_generator
from flask import Flask
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def get_random_int():
    return str(random_int_generator())

if __name__ == '__main__':
    app.run(debug=True)