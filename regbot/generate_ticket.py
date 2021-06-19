from io import BytesIO

import requests
from PIL import Image, ImageDraw, ImageFont, ImageColor

TICKET_TEMPLATE = 'files/reg_template.jpg'

TEXT_COLOR = ImageColor.colormap['blue']
FONT_PATH = 'files/Arial_Cyr.ttf'
FONT_SIZE = 20

NAME_POZ = (165, 265)
EMAIL_POZ = (165, 330)
AVATAR_OFFSET = (50, 280)


def generate_ticket(name, email):
    template = TICKET_TEMPLATE
    ticket_image = Image.open(template)
    draw = ImageDraw.Draw(ticket_image)
    font = ImageFont.truetype(font=FONT_PATH, size=FONT_SIZE)
    coord_texts = [{'coord': NAME_POZ, 'text': name}, {'coord': EMAIL_POZ, 'text': email}]
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

    # with open('files/ticket_example.png', 'wb') as f:
    #     ticket_image.save(f, 'png')


# rez = generate_ticket('Михаил', 'tt23@mail.gv')
# print(rez)
