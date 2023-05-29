from flask import Flask, request, jsonify
from quickstart import Analizar
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/api', methods=['POST','GET'])
def handle_link():
    link = request.json.get('link')

    # response = {'message': 'Enlace recibido con éxito :' + link}
    data = Analizar(link)
    # print(data["Contenido"])
    # print(data["Confianza"])
    # print("El codigo es ", link)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    print(data)
    return jsonify(data)


# @app.route('/api/result', methods=['GET'])
# def show_result():
#     link = request.json.get('link')

#     # response = {'message': 'Enlace recibido con éxito :' + link}
#     data = Analizar(link)
#     print(data["Contenido"])
#     print(data["Confianza"])
#     # print("El codigo es ", link)

#     json_data = {
#         "Contenido": data["Contenido"],
#         "Confianza": data["Confianza"]
#     }

#     # Crear la respuesta en formato JSON
#     response = jsonify({'result': ' Lusti', 'name' : data})

#     # Establecer el tipo de contenido y la codificación de caracteres en la respuesta

#     # Retornar la respuesta
#     return response



if __name__ == '__main__':
    app.run(debug=True)

