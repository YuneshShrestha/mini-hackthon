from flask import Flask, request, jsonify

app = Flask(__name__)

data_storage = [
   
]

@app.route('/scan', methods=['POST'])
def scan_item():
    data = request.json
    item_name = data.get('item_name')
    quantity = data.get('quantity')

    if item_name and quantity:
        data_storage.append({
            'item_name': item_name,
            'quantity': quantity
        })
        return jsonify({"message": "Data received successfully"}), 201
    else:
        return jsonify({"error": "Invalid data"}), 400

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_storage)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
