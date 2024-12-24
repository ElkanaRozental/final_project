def normalize_data(message):
    data = {
        "city": message.get("groq_response", {}).get("city", None),
        "country": message.get("groq_response", {}).get("country", None),
        "latitude": message.get("groq_response", {}).get("latitude", None),
        "longitude": message.get("groq_response", {}).get("longitude", None),
        "description": message.get("body", None),
        "date": message.get("groq_response", {}).get("date", None),
    }
    return data
