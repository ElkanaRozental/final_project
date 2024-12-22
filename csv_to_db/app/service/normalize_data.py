from datetime import date

from app.utils.normalize_utils import normalize_number


def normalize_date(message):
    year = int(message.get('iyear', 0))
    month = int(message["imonth"]) if int(message["imonth"]) > 0 else 1
    day = int(message["iday"]) if int(message["iday"]) > 0 else 1
    the_date = date(year,month,day)
    return {
        "date": the_date
    }

def normalize_city(message):
    return {
        "city": message['city'] if message['city'] else "Unknown",
        "longitude": float(message['longitude']) if message['longitude'] else None,
        "latitude": float(message['latitude']) if message['latitude'] else None,
    }



def normalize_event(message):
    return {
        "kill_number": float(message['nkill']) if message['nkill'] else 0,
        "wound_number": float(message['nwound']) if message['nwound'] else 0,
        "terror_group": message['gname'] if message['gname'] else "Unknown",
        "killers_number": normalize_number(message['nperps']),
        "is_suicide": bool(int(message['suicide'])) if message['suicide'] else None,
    }




def normalize_message(message):
    return {
        "date": normalize_date(message),
        "city": normalize_city(message),
        "country": message['country_txt'],
        "region": message['region_txt'],
        "province": message['provstate'],
        "event": normalize_event(message),
        "target_type": message['targtype1_txt'],
        "attack_type": message['attacktype1_txt'],
    }