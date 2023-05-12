# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of each of the following:
#       - It must be longer than 7 characters (8 is fine)
#       - It must contain at least one of the following special characters:
#         `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==
from datetime import datetime

class PasswordManager2():
    def __init__(self):
      self.service_dict = {}
      self.special_chars = ['!', '@', '$', '%', '&']
    
    def add(self, service, password):
        if (len(password) >= 8 and any(char in password for char in self.special_chars) and password not in self.service_dict.values()):
            if all(password != entry.get('password', None) for entry in self.service_dict.values()):
                self.service_dict[service] = {'password': password, 'added_on' : datetime.now()}

        return None
   
    def remove(self, service):
       self.service_dict.pop(service)

    def update(self, service, new_password):
        current_password = self.service_dict.get(service, None).get('password', None)
        if current_password is not None and (len(new_password) >= 8 and any(char in new_password for char in self.special_chars)):
            if all(new_password != entry.get('password', None) for entry in self.service_dict.values() if entry != self.service_dict[service]):
                self.service_dict[service]['password'] = new_password
                self.service_dict[service]['added_on'] = datetime.now()
        return None
        
                

    def list_services(self):
        return list(self.service_dict.keys())
    
    def sort_services_by(self, sort_by, reverse=False):
        if reverse == 'reverse':
            reverse = True
        else:
            reverse = False
            
        if sort_by == 'service':
            sorted_services = sorted(self.service_dict.keys(), reverse=reverse)
        elif sort_by == 'added_on':
            sorted_services = sorted(self.service_dict.items(), key=lambda x: x[1]['added_on'], reverse=reverse)
            sorted_services = [x[0] for x in sorted_services]
        return sorted_services
        
   
    def get_for_service(self, service):
        return self.service_dict.get(service, {}).get('password', None)