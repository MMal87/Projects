def improve_grammar(text):
    if text == "":
        raise Exception("Please enter some text.")
    return text[0].isupper() and text[-1] in ".!?"


