while maze != []:
  degrees = 1
  while degrees != 0:
    degrees = 0
    if options("down"):
      for i in range(0,100):
        return options.get("down")
      degrees = 0
    elif options.get("right"):
      return options.get("right")
      degrees = 90
    elif options.get("up"):
      return options.get("up")
      degrees = 180
    elif options.get("left"):
      return options.get("left")
      degrees = 270
  while de
    