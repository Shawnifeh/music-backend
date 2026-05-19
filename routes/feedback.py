from flask import Blueprint, request, jsonify

feedback_bp = Blueprint("feedback", __name__)

feedback_list = []

@feedback_bp.route("/feedback", methods=["POST"])
def feedback():

    data = request.json

    feedback_list.append(data["message"])

    print("NEW FEEDBACK:", data["message"])

    return jsonify({"status": "ok"})