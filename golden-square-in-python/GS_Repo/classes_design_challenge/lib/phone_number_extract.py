import re

class PhoneNumberExtractor:
    def __init__(self, diary):
        self._diary = diary

    def extract(self):
        phone_numbers = set()
        for entry in self._diary.all():
            found_numbers = re.findall(r"0[0-9]{10}", entry.contents)
            phone_numbers.update(found_numbers)
        return phone_numbers