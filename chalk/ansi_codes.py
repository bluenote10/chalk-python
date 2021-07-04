from typing import NamedTuple


class Ansi16Code(NamedTuple):
    on: int
    off: int


class Colors:
    black = Ansi16Code(30, 39)
    red = Ansi16Code(31, 39)
    green = Ansi16Code(32, 39)
    yellow = Ansi16Code(33, 39)
    blue = Ansi16Code(34, 39)
    magenta = Ansi16Code(35, 39)
    cyan = Ansi16Code(36, 39)
    white = Ansi16Code(37, 39)


class BgColors:
    bg_black = Ansi16Code(40, 49)
    bg_red = Ansi16Code(41, 49)
    bg_green = Ansi16Code(42, 49)
    bg_yellow = Ansi16Code(43, 49)
    bg_blue = Ansi16Code(44, 49)
    bg_magenta = Ansi16Code(45, 49)
    bg_cyan = Ansi16Code(46, 49)
    bg_white = Ansi16Code(47, 49)


def wrap_ansi_16(code: int, offset: int = 0) -> str:
    return f"\u001b[{code + offset}m"
