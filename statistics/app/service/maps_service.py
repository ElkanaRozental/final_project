import folium

def get_marker_color(fatal_avg, score):

    if fatal_avg - score > 0.5:
        return "green"
    elif fatal_avg - score < -0.5:
        return "red"
    else:
        return "orange"

def get_marker_color_for_percentage(percentage):

    if percentage > 0:
        return "red"
    elif percentage < 0:
        return "green"
    else:
        return "blue"


def map_for_get_mean_fatal_event_for_country(res: list):
    main_map = folium.Map(location=[0, 0], zoom_start=2)
    for loc in res:
        marker_color = get_marker_color(loc["fatal_avg"], loc["score"])
        folium.Marker(
            location=[loc["latitude"], loc["longitude"]],
            tooltip=(
                f"Country: {loc['country']},"
                f" Region: {loc["region"]},"
                f" City: {loc["city"]},"
                f" Fatal Avg: {loc['fatal_avg']},"
                f" Score: {loc['score']},"
            ),
            popup=f"Fatal Avg: {loc['fatal_avg']}",
            icon=folium.Icon(color=marker_color),
        ).add_to(main_map)
    main_map.save("static/mean_fatal_event.html")

    return main_map


def map_for_most_common_terror_group_by_area(res: list):
    main_map = folium.Map(location=[0, 0], zoom_start=2)
    for loc in res:
        folium.Marker(
            location=[loc["latitude"], loc["longitude"]],
            tooltip=(
                loc["group"]
            ),
            popup=f"most common terror group: {loc['most_groups']}",
            icon=folium.Icon(color="red"),
        ).add_to(main_map)
    main_map.save("static/most_common_group.html")

    return main_map


def map_for_event_percentage_change(res: list):
    main_map = folium.Map(location=[0, 0], zoom_start=2)
    for loc in res:
        folium.Marker(
            location=[loc["latitude"], loc["longitude"]],
            tooltip=(
                loc["percentage_change"]
            ),
            popup=(f"Country: {loc['country']},"
                    f" Region: {loc["region"]},"
                    f" City: {loc["city"]}"
            ),
            icon=folium.Icon(color=get_marker_color_for_percentage(loc["percentage_change"])),
        ).add_to(main_map)
    main_map.save("static/event_percentage_change.html")

    return main_map


def map_for_groups_to_one_target_by_area(res: list):
    main_map = folium.Map(location=[0, 0], zoom_start=2)
    max_group = max([data for data in res], key=lambda x: len(x['groups']))
    folium.Marker(
        location=[max_group["latitude"], max_group["longitude"]],
        tooltip=(
            max_group["target"]
        ),
        popup=(f"terror_groups: {max_group['groups']},"
                f" target: {max_group["target"]},"
        ),
        icon=folium.Icon(color="blue"),
    ).add_to(main_map)
    main_map.save("static/groups_to_one_target.html")

    return main_map

