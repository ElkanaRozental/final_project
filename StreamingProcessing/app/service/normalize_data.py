def normalize_date(message):
    return {
        "year": message['iyear'],
        "month": message['imonth'],
        "day": message['iday'],
    }

def normalize_city(message):
    return {
        "city": message['city'],
        "longitude": message['longitude'],
        "latitude": message['latitude'],
    }


def normalize_event(message):
    return {
        "kill_number": message['nkill'],
        "wound_number": message['nwound'],
        "terror_group": message['gname'],
        "killers_number": message['nkillter'],
        "is_suicide": message['suicide']
    }



def normalize_message(message):
    return {
        "date": normalize_date(message),
        "city": normalize_city(message),
        "country": message['country_txt'],
        "region": message['region_txt'],
        "province": message['provstate'],
        "event": normalize_event(message),
        "target_type": message['targetype_txt'],
        "attack_type": message['attacktype_txt'],
    }