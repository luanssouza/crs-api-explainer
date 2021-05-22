from flask import Flask, request

import src.summarizer as sm

app = Flask(__name__)

@app.route("/summarize", methods = ['POST'])
def summarize():
    data = request.json
    return { "movieId": data['movieId'], "explanation": sm.summarize(data['movieId'], data['profileAttributes']) }

if __name__ == "__main__":
    app.run()