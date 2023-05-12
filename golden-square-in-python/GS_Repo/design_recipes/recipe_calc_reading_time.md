1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


2. Design the Function Signature
def calculate_reading_time(text):
    """
    
    Parameters: (list all parameters and their types)
        text: a string that the user wants to calculate reading time for
        
    Returns: (state the return value and its type)
       time in minutes as a float

    """
    pass 

3. Create Examples as Tests

If a 200 word text is given as a parameter, it will return a time of 1 minute

calculate_reading_time("200")
--> 1.0

If a 300 word text is given as a parameter, it will return a time of 1.5

calculate_reading_time("300")
--> 1.5

If an empty string is given as a parameter, it will return an error message 
--> "Please enter some text"




