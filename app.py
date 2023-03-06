
import os

from werkzeug.exceptions import HTTPException
from flask import Flask, request
import logging

import src.summarizer as sm

app = Flask(__name__)

@app.route("/summarize", methods = ['POST'])
def summarize():
    data = request.json
    return { "movieId": data['movieId'], "explanation": sm.summarize(data['movieId'], data['profileAttributes']) }

@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(e)
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return { "description": e.description, "status": e.code }, e.code

    # now you're handling non-HTTP exceptions only
    return { "message" : "Internal Server Error!", "status": 500 }, 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '9090'))