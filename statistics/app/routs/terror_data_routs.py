from flask import Blueprint, request, jsonify

from app.db.database import session_maker
from app.repository.statistics_repository import get_most_fatal_attack_type

terror_data_blueprint = Blueprint("t_data", __name__)


@terror_data_blueprint.route("/phone_tracker/<int:limit>", methods=['GET'])
def get_interactions(limit):
    try:
        res = get_most_fatal_attack_type(session=session_maker, limit=limit)
        print(request.json)
        return jsonify(res), 200
    except Exception as e:
        print(str(e))
        return jsonify(str(e))