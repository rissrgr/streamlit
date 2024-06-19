from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_temperature():
    data = request.get_json()
    temperature = data.get('temperature')
    unit = data.get('unit')

    if temperature is None or unit not in ['Celsius', 'Fahrenheit']:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        temperature = float(temperature)
    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400

    if unit == 'Celsius':
        converted_temp = (temperature * 9/5) + 32
        converted_unit = 'Fahrenheit'
    else:
        converted_temp = (temperature - 32) * 5/9
        converted_unit = 'Celsius'

    return jsonify({'temperature': converted_temp, 'unit': converted_unit}), 200

if __name__ == '__main__':
    app.run(debug=True)
