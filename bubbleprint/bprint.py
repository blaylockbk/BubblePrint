## Brian Blaylock
## October 22, 2021

import textwrap

def bprint(message, messenger="👷🏻‍♂️", width=70, color='blue', align='left'):
    """Bubble Print"""

    if width is None:
        width = 15

    message = textwrap.wrap(message, width)

    min_width = max([len(m) for m in message])

    if width is None:
        width = min_width

    if align == "center":
        fmt = f"^{width-len(message)-2}s"
    elif align == "left":
        fmt = f"<{width-len(message)-2}s"
    elif align == "right":
        fmt = f">{width-len(message)-2}s"

    # Top of Bubble
    print(f" ╭{(width+1)*'─':{fmt}}╮")

    # Text of Bubble
    for m in message:
        print(f" │ {m:{fmt}}   │")

    # Bottom of Bubble and messenger
    if align in ["left", "center"]:
        print(f" ╰╥{(width)*'─':{fmt}}╯")
        print(f" {messenger}")
    if align == "right":
        print(f" ╰{(width)*'─':{fmt}}╥╯")
        print(f" {(width+1)*' ':{fmt}}{messenger}")
