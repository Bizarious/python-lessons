from itertools import product
from typing import Union
import os

SPACE = "     "
PIPE = "|"
UNDER = "_"
MINUS = "-----"
F_SPACE = "  {}  "

def build_legende_top(field_number):
    out = "  " + ((F_SPACE + UNDER) * field_number)
    out = out[:-1] + '\n'
    return out.format(*[i for i in range(field_number)])


def build_pipeline(field_number, current_line=None):
    if current_line is None:
        out = " " * 2
    else:
        out = str(current_line)
        out += " " * (2 - len(str(current_line)))


    for i in range(field_number - 1):
        if current_line is not None:
            out += F_SPACE
        else:
            out += SPACE
        out += PIPE
    # last empty spaces
    if current_line is not None:
        out += F_SPACE + '\n'
    else:
        out += SPACE + '\n'
    return out


def build_minus_line(field_number):
    out = "  "
    for i in range(field_number - 1):
        out += MINUS + PIPE
    # last minuses
    out += MINUS + '\n'
    return out


def build_field(field_dict, field_number=3):
    out = ""

    # legende top
    out += build_legende_top(field_number)
    # first extra pipe line
    out += build_pipeline(field_number)

    # middle part: minus and pipe lines in succession
    for i in range(field_number - 1):
        out += build_pipeline(field_number, i)
        out += build_minus_line(field_number)

    # last two pipe lines
    out += build_pipeline(field_number, field_number-1)
    out += build_pipeline(field_number)

    # remove last '\n
    out = out[:-1]

    # create format values
    format_values = [field_dict[(x, y)].content for x, y in product(range(field_number), repeat=2)]
    return out.format(*format_values)


class FieldContentError(Exception):
    pass


class FieldCoordError(Exception):
    pass


class Field:

    def __init__(self, *coords: int):
        self._content = " "
        self._coords = coords

    def __repr__(self):
        return self._content

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        if self._content != " ":
            raise FieldContentError("Field is already set")
        if content == "X" or content == "O":
            self._content = content
            return
        raise RuntimeError(f'"{content}" is not a valid character')

    @property
    def coords(self):
        return self._coords


class Board:

    def __init__(self, *, board_size: int = 3):
        self._fields = {}
        self._board_size = board_size
        for i, j in product(range(board_size), repeat=2):
            self._fields[(i, j)] = Field(i, j)

    def __repr__(self):
        return build_field(self._fields, self._board_size)

    def set_field(self, content: str, coords: tuple):
        if coords not in self._fields:
            raise FieldCoordError()
        self._fields[coords].content = content

    def check_win(self) -> Union[int, None]:
        x_fields = [field for field in self._fields.values() if field.content == "X"]
        o_fields = [field for field in self._fields.values() if field.content == "O"]

        players = {1: x_fields, 2: o_fields}

        for player, fields in players.items():
            if len(fields) >= self._board_size:
                x = range(self._board_size)
                y = range(self._board_size)

                for x_c in x:
                    if len([field for field in fields if field.coords[0] == x_c]) == self._board_size:
                        print("x")
                        return player

                for y_c in y:
                    if len([field for field in fields if field.coords[1] == y_c]) == self._board_size:
                        print("y")
                        return player

                coords = [(i, i) for i in range(self._board_size)]
                if len([field for field in fields if field.coords in coords]) == self._board_size:
                    print("oben links -> unten rechts")
                    return player

                coords = [(i, self._board_size - i) for i in range(self._board_size)]
                if len([field for field in fields if field.coords in coords]) == self._board_size:
                    print("oben rechts -> unten links")
                    return player

        return None

    def is_full(self) -> bool:
        if len([field for field in self._fields.values() if field.content == " "]) == 0:
            return True
        return False


class TicTacToe:

    def __init__(self, *, board_size: int = 3):
        self._board = Board(board_size=board_size)
        self._chars = {1: "X", 2: "O"}
        self._player = 1

    def play(self):
        while True:
            print(self._board)
            print("\n")

            result = self._board.check_win()
            if result is not None:
                print(f"Spieler {result} gewinnt")
                return

            if self._board.is_full():
                print("Keine freien Felder mehr zur Verfügung")
                return

            x, y = input(f"Spieler {self._player}: ").split()

            while True:
                try:
                    self._board.set_field(self._chars[self._player], (int(x), int(y)))
                except FieldContentError:
                    x, y = input(f"Das Feld ist besetzt, bitte neues eingeben: ").split()
                except FieldCoordError:
                    x, y = input(f"Das Feld existiert nicht, bitte neues eingeben: ").split()
                else:
                    break

            if self._player == 1:
                self._player = 2
            else:
                self._player = 1


if __name__ == "__main__":
    t = TicTacToe(board_size=3)
    t.play()
