#Vulnerable Code
from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/unsafe')
def unsafe():
    name = request.args.get('name')
    return f'Hello {name}, Welcome to Hackmansec'

@app.route('/safe')
def safe():
    name = escape(request.args.get('name'))
    return f'Hello {name}, Welcome to Hackmansec'

if __name__ == '__main__':
    app.run()

