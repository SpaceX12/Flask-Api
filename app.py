from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = []

@app.route("/add-data", methods = ["POST"])

def addData():

    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        }, 400)

    contact={
        'id' : contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'Done':False
    }

    contacts.append(contact)

    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })

if __name__ == "__main__":
    app.run(debug = True)