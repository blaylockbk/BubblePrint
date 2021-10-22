## Brian Blaylock
## October 22, 2021

def bprint(message, character="👷🏻‍♂️"):
    """Balloon Print"""
    print(
        " ╭─────────────────────────────────────────────────╮\n"
       f" │ {message:<45s}   │\n"
        " ╰╥────────────────────────────────────────────────╯\n"
       f" {character}"
    )
