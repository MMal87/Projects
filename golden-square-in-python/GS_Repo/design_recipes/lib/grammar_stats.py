import math
class GrammarStats():
    def __init__(self):
        self.counter_correct = 0
        self.counter_total = 0
  
    def check(self, text):
        
        self.counter_total +=1
        if text[0].isupper() and text[-1] in "!?.":
            self.counter_correct += 1
            return True
            
        return False
        
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        return math.floor(self.counter_correct/self.counter_total  * 100)
    