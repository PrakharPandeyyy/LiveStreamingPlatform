from flask import Flask, jsonify, request, json
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb+srv://PP:qweasd123@cluster0.mb6xwr6.mongodb.net/facebook?retryWrites=true&w=majority"
mongo = PyMongo(app)




if __name__ == "__main__":
    app.run(debug=True)

overlay_schema = {
    'position': str,
    'size': str,
    'content': str,
}

# Routes for CRUD operations on overlays
@app.route('/api/overlays', methods=['POST'])
def create_overlay():
    overlay_data = request.json
    overlay_id = mongo.db.overlays.insert_one(overlay_data).inserted_id
    return jsonify({'message': 'Overlay created', 'id': str(overlay_id)}), 201

@app.route('/api/overlays', methods=['GET'])
def get_overlays():
    overlays = list(mongo.db.overlays.find())
    return jsonify(overlays)

@app.route('/api/overlays/<overlay_id>', methods=['GET'])
def get_overlay(overlay_id):
    overlay = mongo.db.overlays.find_one({'_id': overlay_id})
    if overlay:
        return jsonify(overlay)
    return jsonify({'message': 'Overlay not found'}), 404

@app.route('/api/overlays/<overlay_id>', methods=['PUT'])
def update_overlay(overlay_id):
    overlay_data = request.json
    result = mongo.db.overlays.update_one({'_id': overlay_id}, {'$set': overlay_data})
    if result.modified_count == 1:
        return jsonify({'message': 'Overlay updated'})
    return jsonify({'message': 'Overlay not found'}), 404

@app.route('/api/overlays/<overlay_id>', methods=['DELETE'])
def delete_overlay(overlay_id):
    result = mongo.db.overlays.delete_one({'_id': overlay_id})
    if result.deleted_count == 1:
        return jsonify({'message': 'Overlay deleted'})
    return jsonify({'message': 'Overlay not found'}), 404

