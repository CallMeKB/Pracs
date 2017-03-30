COLOURS = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
           "beige": "#f5f5dc", "black": "#000000", "blanchedalmond": "#ffebcd", "blue1": "#0000ff",
           "blueviolet": "#8a2be2", "brown": "#a52a2a"}

colour = input("Enter colour: ")
while colour != "":
    if colour.lower() in COLOURS:
        print(COLOURS[colour.lower()])
    else:
        print("Invalid colour.")
    colour = input("Enter colour: ")
