from flask import Flask, request, make_response, jsonify
from database import add_participent_to_DB, load_participents, load_participent, update_participant, delete_participant

app = Flask(__name__)


@app.route('/')



@app.route('/create', methods=['POST'])
def join():
	if request.method == 'POST':
		data = request.form
		add_participent_to_DB(data)
		response = make_response("Successfull created a participent", 200)  # Create a response with "Success" message and status code 200
		return response


@app.route('/participants', methods=['GET'])
def participants():
	data = load_participents()
	return data
	# return jsonify(data)  # Convert the data to a JSON response


@app.route('/participant/<name>', methods=['GET'])
def participant(name):
    participant_data = load_participent(name)
    
    if participant_data is None:
        return jsonify({"error": "Participant not found"}), 404
    
    # Convert the participant data to a dictionary and return as JSON response
    participant_dict = {
        "name": participant_data[0],
        "addr": participant_data[1],
        "city": participant_data[2],
        "pin": participant_data[3]
    }
    
    return jsonify(participant_dict)


@app.route('/updateParticipant/<name>', methods=['PUT'])
def update_participant_route(name):
    updates = request.json  # JSON data in the request body

    if updates is None:
        return jsonify({"error": "No update data provided"}), 400

    participant_data = load_participent(name)
    if participant_data is None:
        return jsonify({"error": "Participant not found"}), 404

    if update_participant(name, updates):
        return jsonify({"message": "Participant updated successfully"})
    else:
        return jsonify({"error": "No valid fields to update"}), 400


@app.route('/deleteParticipant/<name>', methods=['DELETE'])
def delete_participant_route(name):
    delete_participant(name)
    return jsonify({"message": f"Participant {name} deleted successfully"})

if __name__ == '__main__':
	app.run(debug=False)
