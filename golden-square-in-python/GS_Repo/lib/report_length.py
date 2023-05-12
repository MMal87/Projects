def report_length(string):
    if not isinstance(string, str):
        print(string)
        return "Incorrect argument given."
    length = len(string)
    return f"This string was {length} characters long."
