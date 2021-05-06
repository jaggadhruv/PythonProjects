print("This is script to work with Images")

from PIL import Image

mac = Image.open("mac.jpg")
print(type(mac))


# #  cropping the image
# print(mac.size)
# mac.crop((0,0,580,400))
# mac.show()
#
# mac.resize((200,50))
# mac.show()

#  Import Images
mask = Image.open("mask.png")
word_matrix = Image.open("word_matrix.png")

print(mask.size)
print(word_matrix.size)

mask = mask.resize((1015,559))
print(mask.size)

mask.putalpha(100)

word_matrix.paste(mask,(0,0),mask)
word_matrix.show()