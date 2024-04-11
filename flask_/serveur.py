from flask import Flask, request, jsonify

app = Flask(__name__)

# Exemple de données stockées en mémoire
data = {}

# Route pour la méthode GET
@app.route('/data/<key>', methods=['GET'])
def get_data(key):
    if key in data:
        return jsonify({key: data[key]})
    else:
        return jsonify({"error": "Clé non trouvée"}), 404

# Route pour la méthode POST
@app.route('/data', methods=['POST'])
def create_data():
    req_data = request.get_json()
    if 'key' in req_data and 'value' in req_data:
        key = req_data['key']
        value = req_data['value']
        data[key] = value
        return jsonify({key: value}), 201
    else:
        return jsonify({"error": "Clé ou valeur manquante"}), 400

# Route pour la méthode PUT
@app.route('/data/<key>', methods=['PUT'])
def update_data(key):
    req_data = request.get_json()
    if key in data:
        data[key] = req_data['value']
        return jsonify({key: data[key]}), 200
    else:
        return jsonify({"error": "Clé non trouvée"}), 404

# Route pour la méthode DELETE
@app.route('/data/<key>', methods=['DELETE'])
def delete_data(key):
    if key in data:
        del data[key]
        return jsonify({"message": "Données supprimées"}), 200
    else:
        return jsonify({"error": "Clé non trouvée"}), 404

if __name__ == '__main__':
    app.run(debug=True)

