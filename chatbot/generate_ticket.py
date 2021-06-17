from PIL import Image, ImageDraw, ImageFont, ImageColor

TICKET_TEMPLATE = 'files/tt.png'
TEXT_COLOR = ImageColor.colormap['blue']
FONT_PATH = 'files/Arial_Cyr.ttf'
FONT_SIZE = 16
DEPARTURE_POZ = (380, 150)
DESTINATION_POZ = (380, 210)
FLIGHT_POZ = (380, 270)
SEATS_POZ = (380, 330)


def generate_ticket(departure, destination, flight, seats):
    template = TICKET_TEMPLATE
    ticket_image = Image.open(template)
    draw = ImageDraw.Draw(ticket_image)
    font = ImageFont.truetype(font=FONT_PATH, size=FONT_SIZE)
    coord_texts = [{'coord': DEPARTURE_POZ, 'text': departure}, {'coord': DESTINATION_POZ, 'text': destination},
                   {'coord': FLIGHT_POZ, 'text': flight}, {'coord': SEATS_POZ, 'text': seats}]
    for info in coord_texts:
        draw.text(info['coord'], info['text'], font=font, fill=TEXT_COLOR)

    ticket_image.save('ticket.png')


generate_ticket('Лондон', 'Брюгге', '23-06-2021 18-20 мп04', '4')
