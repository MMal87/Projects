# == INSTRUCTIONS ==
#
# These challenges are a bit trickier and, in some cases, will required a few
# lines of code. If you start to get a little stuck, take a step back and make
# a plan by breaking the overall task down into small steps.

# == EXERCISES ==

# Purpose: checks if a string starts with the letter a
# Example:
#   Call:    starts_with_the_letter_a("apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Rock")
#   Returns: False
def starts_with_the_letter_a(string):
    if string[0] == "a" or string[0] == "A":
        return True
    else:
        return False


# Purpose: checks if a string ends with the letter a
# Example:
#   Call:    ends_with_the_letter_a("Java")
#   Returns: True
#   Call:    ends_with_the_letter_a("JAVA")
#   Returns: True
#   Call:    ends_with_the_letter_a("Python")
#   Returns: False
def ends_with_the_letter_a(string):
    if string[-1] == "a" or string[-1] == "A":
        return True
    else:
        return False


# Purpose: checks if a string contains the word hello
# Example:
#   Call:    contains_hello("hello world")
#   Returns: True
#   Call:    contains_hello("HELLO WORLD")
#   Returns: True
#   Call:    contains_hello("world")
#   Returns: False
def contains_hello(string):
    if "hello" in string or "HELLO" in string or "Hello" in string:
        return True
    else:
        return False


# Purpose: replaces the word hello with the word goodbye
# Note: you don't need to worry about matching 'Hello' or 'HELLO' here
#       lowercase only is fine.
# Example:
#   Call:    substitute_hello_with_goodbye("hello folks")
#   Returns: "goodbye folks"
#   Call:    substitute_hello_with_goodbye("Hello folks")
#   Returns: "Hello folks"
def substitute_hello_with_goodbye(string):
    new_string = string.replace("hello", "goodbye")
    return new_string
    
        

# Purpose: removes the letter x from a string
# Example:
#   Call:    remove_x("xoxo")
#   Returns: "oo"
#   Call:    remove_x("OXO")
#   Returns: "OO"
def remove_x(string):
    new_string = string.replace("x", "").replace("X", "")
    return new_string

            


# Purpose: returns the first half of a string
# Example:
#   Call:    first_half("coding")
#   Returns: "cod"
# Note: you can assume the string will always have an even number of characters
def first_half(string):
    fstring = ""
    lstring = ""
    for i in range(0,len(string)):
        if i <= len(string) // 2-1:
            fstring += string[i]
        else:
            lstring += string[i]
    return fstring


# Purpose: returns the second half of a string
# Example:
#   Call:    second_half("coding")
#   Returns: "ing"
# Note: you can assume the string will always have an even number of characters
def second_half(string):
    fstring = ""
    lstring = ""
    for i in range(0,len(string)):
        if i <= len(string) // 2-1:
            fstring += string[i]
        else:
            lstring += string[i]
    return lstring


# Congrats, you're done with this file. Move on to the next one.
