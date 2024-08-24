from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process-data', methods=['POST','GET'])
def process_data():
    # Sample user details
    user_id = "john_doe_17091999"
    email = "john@xyz.com"
    roll_number = "ABCD123"
    
    # Retrieve data from the request
    data = request.json.get('data', [])
    
    # Initialize result lists
    odd_numbers = []
    even_numbers = []
    alphabets = []
    
    # Process the data
    for item in data:
        if isinstance(item, str):
            if item.isdigit():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            elif item.isalpha():
                alphabets.append(item.upper())
    
    # Create the response
    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True,port = 8000)