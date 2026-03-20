from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from model import calculate_nutrition

app = Flask(__name__)
CORS(app)

# 🔥 THIS PART YOU ADD
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    
    weight = data['weight']
    foods = data['foods']

    result = calculate_nutrition(weight, foods)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)