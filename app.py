from flask import Flask, request, jsonify
from models import db, Immigrant
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Create the database
with app.app_context():
    db.create_all()

# CREATE: Add a new immigrant record
@app.route('/immigrants', methods=['POST'])
def add_immigrant():
    data = request.json
    new_immigrant = Immigrant(
        name=data['name'],
        country_of_origin=data['country_of_origin'],
        visa_type=data['visa_type'],
        status=data['status']
    )
    db.session.add(new_immigrant)
    db.session.commit()
    return jsonify({'message': 'New immigrant record created'}), 201

# READ: Get all immigrant records
@app.route('/immigrants', methods=['GET'])
def get_immigrants():
    immigrants = Immigrant.query.all()
    return jsonify([{
        'id': immigrant.id,
        'name': immigrant.name,
        'country_of_origin': immigrant.country_of_origin,
        'visa_type': immigrant.visa_type,
        'status': immigrant.status
    } for immigrant in immigrants])

# READ: Get a single immigrant record by ID
@app.route('/immigrants/<int:id>', methods=['GET'])
def get_immigrant(id):
    immigrant = Immigrant.query.get_or_404(id)
    return jsonify({
        'id': immigrant.id,
        'name': immigrant.name,
        'country_of_origin': immigrant.country_of_origin,
        'visa_type': immigrant.visa_type,
        'status': immigrant.status
    })

# UPDATE: Update an existing immigrant record
@app.route('/immigrants/<int:id>', methods=['PUT'])
def update_immigrant(id):
    data = request.json
    immigrant = Immigrant.query.get_or_404(id)
    immigrant.name = data['name']
    immigrant.country_of_origin = data['country_of_origin']
    immigrant.visa_type = data['visa_type']
    immigrant.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Immigrant record updated'})

# DELETE: Remove an immigrant record
@app.route('/immigrants/<int:id>', methods=['DELETE'])
def delete_immigrant(id):
    immigrant = Immigrant.query.get_or_404(id)
    db.session.delete(immigrant)
    db.session.commit()
    return jsonify({'message': 'Immigrant record deleted'})

if __name__ == '__main__':
    app.run(debug=True)
