import re

class PostcodeChecker():
    def check(self, postcode):
        if postcode is None:
            return False
        return re.match(
            r"[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}",
            postcode,
            re.IGNORECASE) is not None

