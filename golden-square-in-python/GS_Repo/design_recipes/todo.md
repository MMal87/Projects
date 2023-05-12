1. Describe the Problem:

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO


2. Design the Function Signature:

def to_do(string)
check string to see if #TODO is present
returns:
boolean (True/False)

3. Create Examples as Tests

give a list with #TODO at the start
--> TRUE

Give a list with #TODO at the end
-->TRUE

Give a list without #TODO
--> False

give an empty list
--> False