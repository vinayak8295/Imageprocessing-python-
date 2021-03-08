from PIL import Image

filename = "wanda.png"

img = Image.open(filename)
img1 = Image.open(filename)
img2 = Image.open(filename)
img3 = Image.open(filename)



# for rotation
rotation_angle = input("how much degree you want to rotate")
rotation_angle = int(rotation_angle)

img = img.rotate(angle=rotation_angle,expand=True,fillcolor="green")
img.show()

# for resizing

resize_width = input("Enter the factor by how much you want to increase or decrease the width of image")
resize_width = float(resize_width)

resize_height = input("Enter the factor by how much you want to increase or decrease the height of  image")
resize_height = float(resize_height)

img1 = img1.resize((int(img1.width*resize_width),int(img1.height*resize_height)))
img1.show()

# for croping
startingX = input("Enter the X coordinate from where you want to start croping")
startingX = int(startingX)

startingY = input("Enter the Y coordinate from where you want to start croping")
startingY = int(startingY)

Height = input("Enter the Height of croped image")
Height = int(Height)

Width = input("Enter the Width of croped image")
Width = int(Width)

img2 = img2.crop(box=(startingX,startingY,Width,Height))
img2.show()
