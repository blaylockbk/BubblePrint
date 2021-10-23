## Brian Blaylock
## October 22, 2021

import textwrap

_align = dict(left="<", center="^", right=">")
_color = dict(
    blue="\033[94m",
    cyan="\033[96m",
    green="\033[92m",
    red="\033[91m",
    purple="\033[95m",
)

def bprint(message, messenger="👷🏻‍♂️", width=70, color=None, align='left'):
    """Bubble Print"""
    assert color in _color or color is None, f"color must be None or one of {list(_color)}"
    assert align in _align, f"align must be one of {list(_align)}"

    if width is None:
        wrap_width = 15
    else:
        wrap_width = width
    message = textwrap.wrap(message, wrap_width, break_long_words=False)

    if width is None:
        width = max([len(m) for m in message])

    # Top of Bubble
    if color is not None:
        print(_color[color])
    print(f" ╭{(width+2)*'─':{_align[align]}{width}}╮")

    # Text of Bubble
    for m in message:
        if len(m) > width:
            print(f" │ {m:{_align[align]}{width}} ")
        else:
            print(f" │ {m:{_align[align]}{width}} │")

    # Bottom of Bubble and messenger
    if align in ["left", "center"]:
        print(f" ╰╥{(width+1)*'─':{_align[align]}{width}}╯")
        print(f" {messenger}")
    elif align == "right":
        print(f" ╰{(width+1)*'─':{_align[align]}{width}}╥╯")
        print(f" {(width+2)*' ':{_align[align]}{width}}{messenger}")

    if color is not None:
        print("\033[0m")

if __file__ == "__main__":

    long_str = "I'm going to tell you a lot of information in this message, so please read this full message."

    bprint('Hello World!')
    bprint("Hello World, I'm over here!", width=30, align='right')
    bprint('Hello World!', messenger="Me", width=30, align='center')
    bprint('I have a whale of a tale for you.', messenger="🐳", color="blue", width=15, align='center')
    bprint(long_str, width=None, color="red")
    bprint("Here is a website:\nhttps://docs.python.org/3/library/textwrap.html", width=None)
