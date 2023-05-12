1. Describe the Problem
    > As a user
    > So that I can keep track of my music listening
    > I want to add tracks I've listened to and see a list of them.


2. Design the Class Interface

Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

"""
class MusicTracker():
    # User-facing properties:
    #   name: string
    
    def __init__(self):
        # Parameters:
        #   Holds a list that is updated
        pass # No code here yet

    def add_track(self, track):
        # Parameters:
        #   track: string representing the track
        pass # No code here yet

    def view_tracks(self):
        # Parameters:
        #   None
        # Returns:
        #   the list of tracks added
        pass # No code here yet

"""

3. Create Examples as Tests

Make a list of examples of how the class will behave in different situations.

# EXAMPLE
"""
Given an empty list
#add_track raises an exception
"""
musictracker = MusicTracker()
musictracker.add_track("") # raises an error with the message "No track added."

"""
Given one track
#add_track adds the track to our list
"""
musictracker = MusicTracker()
musictracker.add_track("purple rain")
musictracker = MusicTracker() # => adds "purple rain" to list

"""
Given that multiple tracks are added
#add_track will add multiple tracks to the list
musictracker = MusicTracker()
musictracker.add_track("purple rain")
musictracker.add_track("wavin' flag")
musictracker.add_track("when doves cry")
musictracker = MusicTracker() # => [adds to all tracks to this list]

"""
Given one track, it returns the track in a list
#view_tracks allows us to view the tracks in the list
"""
musictracker = MusicTracker()
musictracker.add_track("purple rain")
musictracker.view_tracks()
musictracker = MusicTracker() # => shows us ["purple rain"]

"""
Given multiple tracks, it returns the tracks in a list
#view_tracks allows us to view the tracks in the list
"""
musictracker = MusicTracker()
musictracker.add_track("purple rain")
musictracker.add_track("wavin' flag")
musictracker.add_track("when doves cry")
musictracker.view_tracks()
musictracker = MusicTracker() # => shows us ["purple rain", "wavin' flag", "when doves cry"]

4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.
