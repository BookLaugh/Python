from PIL import Image

mac = Image.open('example.jpg')
new_mac = mac.crop((0,0,100,100))
new_mac.show()

pencils = Image.open("pencils.jpg")
pencils.show()
x = 0
y = 0
w = 1950/3
h = 1300/10
new_pencil = pencils.crop((x,y,w,h))
new_pencil.show()

x = 0
y = 1100
w = 1950/3
h = 1300

new_pencil2 = pencils.crop((x,y,w,h))
new_pencil2.show()

halfway = 1993/2
x = halfway-200
w = halfway+200
y = 800
h = 1257
new_mac = mac.crop((x,y,w,h))
new_mac.show()

mac.paste(im=new_mac,box=(0,0))
mac.paste(im=new_mac,box=(0,800))
mac.paste(im=new_mac,box=(1000,0))
mac.show()
new_mac2 = mac.resize((4000,800))
new_mac2.show()

new_pencils = pencils.rotate(120)
new_pencils.show()
