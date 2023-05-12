def calculate_reading_time(text):
    if text == "":
        raise Exception("Please enter some text.")
    text_length = len(text.split())
    return text_length/200

    

