from itertools import product


SPACE = "     "
PIPE = "|"
MINUS = "-----"
F_SPACE = "  {}  "

def build_pipeline(field_number, with_format=True):
    out = ""
    for i in range(field_number - 1):
        if with_format:
            out += F_SPACE
        else:
            out += SPACE
        out += PIPE
    # last empty spaces
    if with_format:
        out += F_SPACE + '\n'
    else:
        out += SPACE + '\n'
    return out


def build_minus_line(field_number):
    out = ""
    for i in range(field_number - 1):
        out += MINUS + PIPE
    # last minuses
    out += MINUS + '\n'
    return out

def build_field(field_dict, field_number=3):
    out = ""

    # first extra pipe line
    out += build_pipeline(field_number, False)

    # middle part: minus and pipe lines in succession
    for i in range(field_number - 1):
        out += build_pipeline(field_number)
        out += build_minus_line(field_number)

    # last two pipe lines
    out += build_pipeline(field_number)
    out += build_pipeline(field_number, False)

    # remove last '\n
    out = out[:-1]

    # create format values
    format_values = [field_dict[(x, y)] if (x, y) in field_dict.keys() else " " for x, y in product(field_number, repeat=2)]
    return out.format(*format_values)
