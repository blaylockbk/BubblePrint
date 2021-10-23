# 💬 Bubble Print

Give your print statements personality. Print dialoge in speach bubbles.

```python
from bubbleprint import bprint

bprint("Hello World!")
bprint('I have a whale of a tale for you.', messenger="🐳", color="blue", width=15, align='center')
bprint("Here is a website:\nhttps://docs.python.org/3/library/textwrap.html", width=None)
```
```
OUT:
 ╭────────────────────────────────────────────────────────────────────────╮
 │ Hello World!                                                           │
 ╰╥───────────────────────────────────────────────────────────────────────╯
 👷🏻‍♂️

 ╭─────────────────╮
 │ I have a whale  │
 │  of a tale for  │
 │      you.       │
 ╰╥────────────────╯
 🐳

 ╭─────────────────────────────────────────────────╮
 │ Here is a                                       │
 │ website:                                        │
 │ https://docs.python.org/3/library/textwrap.html │
 ╰╥────────────────────────────────────────────────╯
 👷🏻‍♂️
 ```
