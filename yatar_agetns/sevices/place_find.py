from models.Response_model import place_find

place_data = [
    place_find(name="Taj Mahal", city="Agra", pincode=282001, rating=4.9),
    place_find(name="Gateway of India", city="Mumbai", pincode=400001, rating=4.7),
    place_find(name="Qutub Minar", city="New Delhi", pincode=110030, rating=4.6),
    place_find(name="Golden Temple", city="Amritsar", pincode=143006, rating=4.9),
    place_find(name="Hawa Mahal", city="Jaipur", pincode=302002, rating=4.6),
    place_find(name="Amer Fort", city="Jaipur", pincode=302028, rating=4.7),
    place_find(name="Red Fort", city="New Delhi", pincode=110006, rating=4.5),
    place_find(name="Victoria Memorial", city="Kolkata", pincode=700071, rating=4.7),
    place_find(name="Meenakshi Temple", city="Madurai", pincode=625001, rating=4.8),
    place_find(name="Charminar", city="Hyderabad", pincode=500002, rating=4.5),
    place_find(name="Mysore Palace", city="Mysuru", pincode=570001, rating=4.8),
    place_find(name="Virupaksha Temple", city="Hampi", pincode=583239, rating=4.7),
    place_find(name="Ajanta Caves", city="Aurangabad", pincode=431117, rating=4.7),
    place_find(name="Basilica of Bom Jesus", city="Old Goa", pincode=403402, rating=4.5),
    place_find(name="Kashi Vishwanath Temple", city="Varanasi", pincode=221001, rating=4.8),
    place_find(name="Brihadisvara Temple", city="Thanjavur", pincode=613009, rating=4.8),
    place_find(name="Pangong Tso", city="Leh", pincode=194101, rating=4.9),
    place_find(name="Sun Temple", city="Konark", pincode=752111, rating=4.7),
    place_find(name="Jallianwala Bagh", city="Amritsar", pincode=143001, rating=4.6),
    place_find(name="India Gate", city="New Delhi", pincode=110001, rating=4.7)
]


async def get_place(city: str):
    """Find places whose city matches the requested city name."""
    if not city or not city.strip():
        return []

    city_name = city.strip().casefold()
    return [
        place
        for place in place_data
        if place.city.casefold() == city_name
    ]

    
