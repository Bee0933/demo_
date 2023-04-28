import random

def get(val:int):
      random_value = random.randint(0,50)
      return (random_value * 2 if isinstance(val, int) else
              ValueError('value input is an integer'))

print(get(3))