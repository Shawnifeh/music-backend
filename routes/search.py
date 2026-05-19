from flask import Blueprint, request, jsonify

search_bp = Blueprint("search", __name__)

songs = [
    {"id": "1", "name": "Parallel Horizon"},
    {"id": "2", "name": "Ghost Circuit"},
    {"id": "3", "name": "CosmicShift"},
    {"id": "4", "name": "Fading Signals"},
    {"id": "5", "name": "Wistful IceCave"},
    {"id": "6", "name": "Song 0"}
]

@search_bp.route("/search")
def search():

    query = request.args.get("q", "").lower()

    results = [
        song for song in songs
        if query in song["name"].lower()
    ]

    return jsonify(results)