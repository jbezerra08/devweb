from flask import Flask, jsonify, request
from api import app

hoteis = [
    {
        "hotel_id": 1,
        "nome": "Alpha Hotel",
        "estrelas": 4.3,
        "diaria": 420.34,
        "cidade": "Rio de Janeiro"
    },
    {
        "hotel_id": 2,
        "nome": "Bravo Hotel",
        "estrelas": 4.4,
        "diaria": 380.90,
        "cidade": "Santa Catarina"
    },{
        "hotel_id": 3,
        "nome": "Charlie Hotel",
        "estrelas": 3.9,
        "diaria": 320.20,
        "cidade": "Fortaleza"
    }
]


@app.route("/")
@app.route("/home")
def main() :
    return jsonify(hoteis)

@app.route("/api/hoteis", methods=["GET"])
def get_hoteis() :
    return jsonify({"nome": hoteis})

@app.route("/api/hoteis/<int:hotel_id>", methods=["GET"])
def get_hotel(hotel_id) :
    return jsonify(hoteis[hotel_id -1]["nome"])

@app.route("/api/hoteis", methods=["POST"])
def add_hotel() :
    try :
        hotel = request.get_json()
        hoteis.append(hotel)
        return jsonifly(hotel), 201
    except IndexError:
        return "erro"

@app.route("/api/hoteis/<int:hotel_id>", methods=["PUT"])
def update_hotel():
    pass

@app.route("/api/hoteis/<int:hotel_id>", methods=["DELETE"])
def delete_hotel():
    pass