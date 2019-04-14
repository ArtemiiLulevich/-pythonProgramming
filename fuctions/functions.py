def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(text, sep=' ', end_char='\n', file=None, flush=False):
    text = ""
    for arg in text:
        text += str(arg) + end_char
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end_char, file=file, flush=flush)


center_text("sfdgdfgd")
center_text("spam, spam, eggs and spam")
center_text(12)
center_text(1, 2, 5, "print", end_char=' ')
