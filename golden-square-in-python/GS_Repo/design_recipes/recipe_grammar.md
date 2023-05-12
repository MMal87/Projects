1. Describe the Problem:

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

2. Design the Function Signature:


def improve_grammar(text)
Take first letter in text and check if it is capitalized
Take last item in text and verify if it is a punctuation mark 

returns:
boolean (True/False)


3. Create Examples as Tests

Gives text with a capital letter at the start and punctuation at the end.
improve_grammar("Hello, world!")
--> True

Gives text without a capital letter or punctuation at the end.
improve_grammar("hello, world")
--> False

Gives text without a capital letter, but with punctuation at the end.
improve_grammar("hello, world!")
--> False

Gives text with a capital letter at the start, but no punctuation at the end.
improve_grammar("Hello, world")
--> False

Gives an empty string as a parameter
improve_grammar("")
--> Error Message- "Please enter some text."





