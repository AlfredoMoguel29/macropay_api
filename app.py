from flask import Flask, jsonify, request, make_response
from utils import sorted_list
import settings

#Initilize app (online)
app = Flask(__name__)

# Loading database
list = sorted_list()

@app.route('/contacts', methods = ['GET'])
def index():
    """
    Index endpoint, returns an ordered list deppending on phrase parameter.
    """
    # parameter phrase doesn't exist
    if "phrase" not in request.args:
        resp = make_response(jsonify(list), 200)
        resp.headers['Content-Type'] = 'application/json'
        return resp
    
    phrase = request.args.get('phrase')
    # parameter exists but is empty
    if phrase == "":
        resp = make_response("", 404)
        return resp

    print('Prueba')
    print('Probando ramas')

    # parameter exists
    else:
        matching_list = [person for person in list if phrase in person['name'].lower()]
        resp = make_response(jsonify(matching_list), 200)
        resp.headers['Content-Type'] = 'application/json'
        return resp

@app.route('/contacts/<contact_id>', methods = ['GET'])
def search_id(contact_id):
    """
    search a person given it's ID.
    """
    matching_list = [person for person in list if contact_id == person['id']]
    # The ID exists
    if len(matching_list) > 0:
        resp = make_response(jsonify(matching_list), 200)
        resp.headers['Content-Type'] = 'application/json'
        return resp
    #The ID doesn't exists
    else:
        resp = make_response("", 404)
        return resp

@app.route('/contact/', methods = ['POST'])
def add_contact():
    """
    Add a new contact with post method.
    """
    new_contact = {
        "id": request.json['id'],
        "name": request.json['name'],
        "phone": request.json['phone'],
        "addressLines": request.json['addressLines'],
    }
    list.append(new_contact)
    print("Contact created by ip: ", request.remote_addr)
    return jsonify({"ip":request.remote_addr, "new_contact":new_contact})

def page_not_found(error):
    """
    Handles not founded pages.
    """
    resp = make_response("", 404)
    return resp

def unexpected_method(error):
    """
    Handles not matching methods.
    """
    resp = make_response("", 405)
    return resp

if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, unexpected_method)
    app.run(debug = settings.API_DEBUG)