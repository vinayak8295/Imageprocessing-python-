from PIL import Image, ImageOps

filename = "wanda.png"

img = Image.open(filename)
img1 = Image.open(filename)
img2 = Image.open(filename)
img3 = Image.open(filename)
img4 = Image.open(filename)
img5 = Image.open(filename)
img6 = Image.open(filename)

#for rotation
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

#Horizontal reflection
img3 = ImageOps.mirror(img3)
img3.show()

#Vertical reflection

img4 = ImageOps.flip(img4)
img4.show()

# Read pixels and apply negative transformation

for i in range(0, img5.size[0] - 1):
    for j in range(0, img5.size[1] - 1):
        # Get pixel value at (x,y) position of the image

        pixelColorVals = img5.getpixel((i, j));

        # Invert color

        redPixel = 255 - pixelColorVals[0];  # Negate red pixel

        greenPixel = 255 - pixelColorVals[1];  # Negate green pixel

        bluePixel = 255 - pixelColorVals[2];  # Negate blue pixel

        # Modify the image with the inverted pixel values

        img5.putpixel((i, j), (redPixel, greenPixel, bluePixel));

# Display the negative image

img5.show();

# Convert RGB image into Black And White
img6 = img6.convert('1')
img6.show();