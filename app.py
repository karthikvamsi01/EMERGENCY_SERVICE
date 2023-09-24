from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize a list to store emergency reports
emergency_reports = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form
        location = request.form['location']
        description = request.form['description']

        # Create an emergency report dictionary
        report = {
            'location': location,
            'description': description
        }

        # Add the report to the list
        emergency_reports.append(report)

    return render_template('index.html', reports=emergency_reports)

@app.route('/api/first_aid_tips', methods=['GET'])
def get_first_aid_tips():
    # Basic first aid tips (you can expand this)
    first_aid_tips = [
        "In case of bleeding, apply pressure to the wound with a clean cloth.",
        "If someone is unconscious, check for breathing and start CPR if needed.",
        "For burns, cool the affected area with cold water for at least 10 minutes.",
        "If someone is choking, perform the Heimlich maneuver.",
        "In case of a fracture, immobilize the injured limb and seek medical help."
    ]
    
    return jsonify({"first_aid_tips": first_aid_tips})

if __name__ == '__main__':
    app.run(debug=True)
