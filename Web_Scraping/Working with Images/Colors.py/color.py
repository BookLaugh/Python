from PIL import Image

blue = Image.open("blue_color.png")
red = Image.open("red_color.jpg")
orange = Image.open("Orange.png")
yellow = Image.open("yellow.png")
brown = Image.open("brown.png")
green = Image.open("green.png")

blue.putalpha(128)
red.putalpha(128)
blue.paste(red,box=(0,0),mask=red)
blue.show()

orange.putalpha(128)
green.putalpha(128)
orange.paste(green,box=(0,0),mask=green)
orange.show()

yellow.putalpha(128)
brown.putalpha(128)
yellow.paste(brown,box=(0,0),mask=brown)
yellow.show()
