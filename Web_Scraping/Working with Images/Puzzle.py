# NOTE: First make sure to pip install pillow

from PIL import Image

matrix = Image.open("word_matrix.png")
mask = Image.open("mask.png")

matrix.paste(mask,(0,0),mask)
# matrix.show()
new_mask = mask.resize((1015,559))
# new_mask.show()
new_mask.putalpha(200)

matrix.paste(new_mask,(0,0),new_mask)
matrix.show()

matrix.save("Puzzle.png")
