import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# Request:
# GET /hello?name=David

# @app.route('/hello', methods=['GET'])
# def hello():
#     name = request.args['name'] # The value is 'David'

#     # Send back a friendly greeting with the name
#     return f"Hello {name}!"

# @app.route('/goodbye', methods=['POST'])
# def goodbye():
#     name = request.form['name'] # The value is 'Alice'

#     # Send back a fond farewell with the name
#     return f"Goodbye {name}!"

# # Request:
# @app.route('/submit', methods = ['POST'])
# def submit():
#     name = request.form['name'] #the value is Leo
#     message = request.form['message'] #the value is "Hello world"

#     return f"Thanks {name}, you sent this message: \"{message}\" "

# @app.route('/wave', methods=['GET'])
# def wave():
#     name = request.args['name']

#     return f"I am waving at {name}"

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    vowels = [char for char in text if char.lower() in 'aeiou']
    vowel_count = len(vowels)
    return f"There are {vowel_count} vowels in \"{text}\""

@app.route('/sort-names', methods=['POST'])
def sort_names():
    names = request.form['names']
    sorted_string = ','.join(sorted(names.split(',')))
    return sorted_string

# To make a request, run:
# curl "http://localhost:5000/hello?name=David"

# # These lines start the server if you run this file directly
# # They also start the server configured to use the test database
# # if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

