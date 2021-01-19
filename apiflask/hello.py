from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/form_to_json', methods=['POST']) 
def form_to_json():
    data = request.json
    return jsonify(data)
    print (data)


'''
quarks = [{'name': 'up', 'charge': '+2/3'},
          {'name': 'down', 'charge': '-1/3'},
          {'name': 'charm', 'charge': '+2/3'},
          {'name': 'strange', 'charge': '-1/3'}]

@app.route("/quarks", methods=["POST"])
def addOne ():
    new_quark = request.get_json ()
    quarks.append (new_quark)
    return jsonify ({'quarks': quarks})
'''


#def insert_new():
    #json_request = request.get_json() # Recupera o JSON enviado
    # Acessando propriedade json_request["id_time"]

    # Montando retorno da operação, caso seja necessário
    #return jsonify({"status": "ok", "obj": obj})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
