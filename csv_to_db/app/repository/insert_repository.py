from app.models import TheDate, City, Country, TargetType, AttackType, Region, Event, Province
# def insert_normalized_message(normalized_message, session):
#     with session() as session:
#         try:
#             date_data = normalized_message['date']['date']
#             date = (
#                 session.query(TheDate)
#                 .filter_by(date=date_data)
#                 .first()
#             )
#             if not date:
#                 date = TheDate(date=date_data)
#                 session.add(date)
#                 session.flush()
#
#             city_data = normalized_message['city']
#             city = (
#                 session.query(City)
#                 .filter_by(city=city_data['city'], longitude=city_data['longitude'], latitude=city_data['latitude'])
#                 .first()
#             )
#             if not city:
#                 city = City(**city_data)
#                 session.add(city)
#                 session.flush()
#
#             country_name = normalized_message['country']
#             country = session.query(Country).filter_by(country=country_name).first()
#             if not country:
#                 country = Country(country=country_name)
#                 session.add(country)
#                 session.flush()
#
#             region_name = normalized_message['region']
#             region = session.query(Region).filter_by(region=region_name).first()
#             if not region:
#                 region = Region(region=region_name)
#                 session.add(region)
#                 session.flush()
#
#             province_name = normalized_message['province']
#             province = session.query(Province).filter_by(province=province_name).first()
#             if not province:
#                 province = Province(province=province_name)
#                 session.add(province)
#                 session.flush()
#
#             target_type_name = normalized_message['target_type']
#             target_type = session.query(TargetType).filter_by(target_type=target_type_name).first()
#             if not target_type:
#                 target_type = TargetType(target_type=target_type_name)
#                 session.add(target_type)
#                 session.flush()
#
#             attack_type_name = normalized_message['attack_type']
#             attack_type = session.query(AttackType).filter_by(attack_type=attack_type_name).first()
#             if not attack_type:
#                 attack_type = AttackType(attack_type=attack_type_name)
#                 session.add(attack_type)
#                 session.flush()
#
#             event_data = normalized_message['event']
#             event = Event(
#                 **event_data,
#                 date_id=date.id,
#                 city_id=city.id,
#                 country_id=country.id,
#                 region_id=region.id,
#                 province_id=province.id,
#                 target_type_id=target_type.id,
#                 attack_type_id=attack_type.id,
#             )
#             session.add(event)
#             session.commit()
#             print(f"Inserted event with ID: {event.id}")
#         except Exception as e:
#             session.rollback()
#             print(f"Error inserting message: {e}")


def insert_normalized_message(normalized_message, session):
    kill_number = float(normalized_message['event'].get('kill_number', 0))
    wound_number = float(normalized_message['event'].get('wound_number', 0))
    terror_group = normalized_message['event'].get('terror_group', '')
    killers_number = int(normalized_message['event'].get('killers_number', 0))
    is_suicide = bool(normalized_message['event'].get('is_suicide', False))
    with session() as session:
        try:
            date = TheDate(date=normalized_message['date']['date'])
            city = City(
                city=normalized_message['city']['city'],
                longitude=normalized_message['city']['longitude'],
                latitude=normalized_message['city']['latitude'],
            )
            country = Country(country=normalized_message['country'])
            region = Region(region=normalized_message['region'])
            province = Province(province=normalized_message['province'])
            target_type = TargetType(target_type=normalized_message['target_type'])
            attack_type = AttackType(attack_type=normalized_message['attack_type'])

            event = Event(
                kill_number=kill_number,
                wound_number=wound_number,
                terror_group=terror_group,
                killers_number=killers_number,
                is_suicide=is_suicide,
                date=date,
                city=city,
                country=country,
                region=region,
                province=province,
                target_type=target_type,
                attack_type=attack_type,
            )

            session.add(event)
            session.commit()
            print(f"Inserted event with ID: {event.id}")

        except Exception as e:
            session.rollback()
            print(f"Error inserting message: {e}")
