from flask import Flask, request
from flask import jsonify
import json

app = Flask(__name__)

@app.route("/webservice", methods=["POST"])
def result():
    print ("Json:", request.is_json)
    content = request.get_json()
    print (content['name'])
    print("Dados recebidos: ", json.loads(request.data))  # raw data
    nome = request.json['name'] # json (if content-type of application/json is sent with the request)
    if not nome or nome == "0": #verifica se a variavel está vazia
        print ("Variavel vazia")
    else:
        print ("NOME: ", nome)

    print("OK: ", request.get_json(force=True))  # json (if content-type of application/json is not sent)
    #return json.dumps({'Sucesso':True}), 200, {'ContentType':'application/json'}  

    data = request.json

    return jsonify(data)
    print ("Result: ",jsonify(data['name']))

    #return 'OK'

    #return "Received !" 


if __name__ == "__main__":
    app.run(debug=True, port=5000)
