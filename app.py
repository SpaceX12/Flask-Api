from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id':1,
        'Name':"Ishan",
        'Contact':123456789,
        'Done':True
    }
]

@app.route("/add-data", methods = ["POST"])

def addData():

    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        }, 400)

    contact={
        'id' : "",
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'Done':False
    }

    contacts.append(contact)

    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })

@app.route("/get-data")
def getContacts():
    return jsonify({
        "data": contacts
    })


if __name__ == "__main__":
    app.run(debug = True)