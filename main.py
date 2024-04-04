"""
This script is serving the flask api for Product Pattern Recognition using Gemini APIs for gemini vision pro:
- /home: this route is just for testing purposes.
- /get_pattern: is used for the following:
    - downloads the image from the given url
    - using gemini to get the product pattern and other stuff.
"""
# Imports are written here
import os
import logging

from dotenv import load_dotenv
from flask import Flask, jsonify

# loading flask
app = Flask(__name__)

# loading env
load_dotenv()

# Set up logging
logging.basicConfig(filename=os.getenv("LOG_FILE"),
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# first route / testing route
@app.route('/home', methods=['GET'])
def get_route():
    logging.info('Testing route accessed.')
    return jsonify({"message": "Working..!"}), 200


if __name__ == '__main__':
    app.run(debug=False,
            host="0.0.0.0",  # server's host
            port=5001)  # port is set to 5001
    logging.info("API Started")
