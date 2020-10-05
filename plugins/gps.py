from userge import userge, Message
from geopy.geocoders import Nominatim


@userge.on_cmd("gps", about={
    'header': "locate the coordinates of addresses, cities, countries, and landmarks",
    'usage': "{tr}gps [location]\ne.g {tr}gps 175 5th Avenue NYC"})
async def gps_locate_(message: Message):
    loc_ = message.input_str
    if not loc_:
        return await message.err('Provide a valid location name', del_in=5)
    await message.edit("Finding This Location In Maps Server.....")
    titlex = None
    if '|' in loc_:
        loc_x = loc_.split('|', 1)
        if len(loc_x) == 2:
            titlex = loc_x[0]
            loc_ = loc_x[1]
    geolocator = Nominatim(user_agent="USERGE-X")
    geoloc = geolocator.geocode(loc_)
    if not geoloc:
        return await message.err('**404 Location Not Found**', del_in=5)
    address = geoloc.address
    place = address.split(",")
    name = titlex if titlex else place[0]
    lon = geoloc.longitude
    lat = geoloc.latitude
    await message.delete()
    reply = message.reply_to_message
    reply_id = reply.message_id if reply else None
    await message.client.send_venue(
        message.chat.id, 
        lat, 
        lon,
        name, 
        address,
        reply_to_message_id=reply_id
    )