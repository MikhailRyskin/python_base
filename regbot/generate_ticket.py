from PIL import Image, ImageDraw, ImageFont, ImageColor

TICKET_TEMPLATE = 'files/reg_template.jpg'
TEXT_COLOR = ImageColor.colormap['blue']
FONT_PATH = 'files/Arial_Cyr.ttf'
FONT_SIZE = 20
NAME_POZ = (165, 265)
EMAIL_POZ = (165, 330)


def generate_ticket(name, email):
    template = TICKET_TEMPLATE
    ticket_image = Image.open(template)
    draw = ImageDraw.Draw(ticket_image)
    font = ImageFont.truetype(font=FONT_PATH, size=FONT_SIZE)
    coord_texts = [{'coord': NAME_POZ, 'text': name}, {'coord': EMAIL_POZ, 'text': email}]
    for info in coord_texts:
        draw.text(info['coord'], info['text'], font=font, fill=TEXT_COLOR)

    ticket_image.save('ticket.png')


generate_ticket('Михаил', 'tt23@mail.gv')
