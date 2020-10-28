class Timer:

    def __init__(self):
        self.secs = ClockHand(60)
        self.hunds = ClockHand(100)

    def advance(self):
      self.hunds.advance()
      if(self.hunds.get_value()==0):
        self.secs.advance()

    def __str__(self):
      return str(self.secs) + ":" + str(self.hunds)

if __name__ == '__main__':
  from clock_hand import ClockHand

else:
  from src.clock_hand import ClockHand
  
