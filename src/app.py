#!/usr/bin/env python
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return "Hello, {}!".format(escape(name))

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')