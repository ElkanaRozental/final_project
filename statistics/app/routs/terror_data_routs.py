import webbrowser

from flask import Blueprint, request, jsonify

from app.db.database import session_maker
from app.repository.statistics_repository import get_most_fatal_attack_type, get_mean_fatal_event_for_area, \
    get_most_common_terror_group_by_area, get_event_percentage_change, get_casualties_killers_correlation, \
    get_groups_with_same_target_by_area
from app.service.maps_service import map_for_get_mean_fatal_event_for_country, map_for_most_common_terror_group_by_area, \
    map_for_event_percentage_change, map_for_groups_to_one_target_by_area
from app.service.pandas_service import calculate_correlation_from_results, calculate_percentage_change_attacks_by_region

terror_data_blueprint = Blueprint("t_data", __name__)


@terror_data_blueprint.route("/most_fatal_attack/<int:limit>", methods=['GET'])
def get_most_fatal_attack(limit):
    try:
        res = get_most_fatal_attack_type(session=session_maker, limit=limit)

        return jsonify(res), 200
    except Exception as e:
        print(str(e))
        return jsonify(str(e))

@terror_data_blueprint.route("/mean_fatal_event", methods=['POST'])
def map_get_mean_fatal_event_for_area():
    try:
        data = request.get_json()
        res = get_mean_fatal_event_for_area(
            session=session_maker,
            limit=data.get("limit"),
            country=data.get("country"),
            province=data.get("province"),
            region=data.get("region"),
            city=data.get("city"),
        )
        map_for_get_mean_fatal_event_for_country(res)
        webbrowser.open("C:/Users/rozen/PycharmProjects/final_test/statistics/app/static/mean_fatal_event.html")
        return jsonify(res), 200
    except Exception as e:
        print(str(e))
        return jsonify(str(e))


@terror_data_blueprint.route("/most_common_group", methods=['POST'])
def map_most_common_group_for_area():
    try:
        data = request.get_json()
        res = get_most_common_terror_group_by_area(
            session=session_maker,
            limit=data.get("limit"),
            country=data.get("country"),
            province=data.get("province"),
            region=data.get("region"),
            city=data.get("city"),
        )
        map_for_most_common_terror_group_by_area(res)
        webbrowser.open("C:/Users/rozen/PycharmProjects/final_test/statistics/app/static/most_common_group.html")
        return jsonify(res), 200
    except Exception as e:
        print(str(e))
        return jsonify(str(e))


@terror_data_blueprint.route("/event_percentage_change", methods=['POST'])
def map_event_percentage_change():
    try:
        data = request.get_json()
        res = get_event_percentage_change(
            session=session_maker,
            limit=data.get("limit"),
            country=data.get("country"),
            province=data.get("province"),
            region=data.get("region"),
            city=data.get("city"),
        )
        res = calculate_percentage_change_attacks_by_region(res)
        map_for_event_percentage_change(res)
        webbrowser.open("C:/Users/rozen/PycharmProjects/final_test/statistics/app/static/event_percentage_change.html")
        return jsonify(res), 200
    except Exception as e:
        print(str(e))
        return jsonify(str(e))


@terror_data_blueprint.route("/casualties_killers_correlation", methods=['GET'])
def casualties_killers_correlation():
    try:
        res = get_casualties_killers_correlation(session=session_maker)
        correlation = calculate_correlation_from_results(res, res, "killers_number", "casualties")
        return jsonify(correlation), 200
    except Exception as e:
        print(str(e))
        return jsonify(str(e))


@terror_data_blueprint.route("/groups_with_same_target", methods=['POST'])
def groups_with_same_target():
    try:
        data = request.get_json()
        res = get_groups_with_same_target_by_area(
            session=session_maker,
            limit=data.get("limit"),
            country=data.get("country"),
            province=data.get("province"),
            region=data.get("region"),
            city=data.get("city"),
        )
        map_for_groups_to_one_target_by_area(res)
        webbrowser.open("C:/Users/rozen/PycharmProjects/final_test/statistics/app/static/groups_to_one_target.html")
        return jsonify(res), 200
    except Exception as e:
        print(str(e))
        return jsonify(str(e))