from flask import Flask, render_template
from json import load

app = Flask(__name__)

@app.route('/items')
def items():
    with open('items.json') as f:
        items = load(f)["items"]
    return render_template('items.html', items=items)

app.run(port=5000, debug=True)