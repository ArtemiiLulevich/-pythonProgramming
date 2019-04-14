def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=' ', end_char='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    # print(" " * left_margin, text, end=end_char, file=file, flush=flush)
    return " " * left_margin + text


# with open("centered", mode='w') as centered_file:
#     center_text("sfdgdfgd", file=centered_file)
#     center_text("spam, spam, eggs and spam", file=centered_file)
#     center_text(12, file=centered_file)
#     center_text(1, 2, 5, "print", file=centered_file)
print(center_text("sfdgdfgd"))
print(center_text("spam, spam, eggs and spam"))
print(center_text(12))
print(center_text(1, 2, 5, "print"))
