def get(val:int):
      return (val * 2 if isinstance(val, int) else
              ValueError('value input is an integer'))

print(get(3))