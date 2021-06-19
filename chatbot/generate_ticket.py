import requests
from PIL import Image, ImageDraw, ImageFont, ImageColor
from io import BytesIO

TICKET_TEMPLATE = 'files/t_template.jpg'
TEXT_COLOR = ImageColor.colormap['blue']
FONT_PATH = 'files/Arial_Cyr.ttf'
FONT_SIZE = 16
DEPARTURE_POZ = (380, 150)
DESTINATION_POZ = (380, 210)
FLIGHT_POZ = (380, 270)
SEATS_POZ = (380, 330)
AVATAR_OFFSET = (50, 230)


def generate_ticket(departure, destination, flight, seats):
    template = TICKET_TEMPLATE
    ticket_image = Image.open(template)
    draw = ImageDraw.Draw(ticket_image)
    font = ImageFont.truetype(font=FONT_PATH, size=FONT_SIZE)
    coord_texts = [{'coord': DEPARTURE_POZ, 'text': departure}, {'coord': DESTINATION_POZ, 'text': destination},
                   {'coord': FLIGHT_POZ, 'text': flight}, {'coord': SEATS_POZ, 'text': str(seats)}]
    for info in coord_texts:
        draw.text(info['coord'], info['text'], font=font, fill=TEXT_COLOR)

    response = requests.get(url='https://www.gravatar.com/avatar/HASH')
    avatar_like_file = BytesIO(response.content)
    avatar = Image.open(avatar_like_file)
    ticket_image.paste(avatar, AVATAR_OFFSET)

    temp_file = BytesIO()
    ticket_image.save(temp_file, 'png')
    temp_file.seek(0)

    return temp_file
