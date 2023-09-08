from flask import Flask, request, jsonify

app = Flask(__name__)

user_info = {
    "full_name_ddmmyyyy": "renny_sam_18092002",
    "email": "rs1563@srmist.edu.in",
    "roll_number": "RA2011003010026",
}

def find_highest_alphabet(data):
    alphabets = [char for char in data if char.isalpha()]
    return [max(alphabets, key=lambda x: x.lower())] if alphabets else []

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        request_data = request.json
        data = request_data.get('data', [])

        response_data = {
            "is_success": True,
            "user_id": user_info["full_name_ddmmyyyy"],
            "email": user_info["email"],
            "roll_number": user_info["roll_number"],
            "numbers": [x for x in data if x.isnumeric()],
            "alphabets": [x for x in data if x.isalpha()],
            "highest_alphabet": find_highest_alphabet(data),
        }
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run()
