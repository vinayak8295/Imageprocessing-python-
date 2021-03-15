"""
--------------------------------------------------------------
                    IMAGE PROCESSING APP
--------------------------------------------------------------
    Client: Imgix
    
    Developers:
        Vinayak Chachra     - 191210061
        Mohammad Shahanwaz  - 191210029
    
    Problem Statement: 
    Image processing project in which user can input any
    image file type and manipulate with that.

    Features:
    1)Colour image into a grayscale image (black & white image)
    2)Compute the average grayscale value of an image
    3)Extract a sub-image from an image (crop image)
    4)Reflect an image in horizontal or vertical directions
    5)Use the filters to enhance the image quality
    6)Enlarge or shrink an image
    7)Translate and rotate an image by amount t & Ө resp.
    8)Image morphing (Compute the sum of two images)
    9)Change detection (Compute the difference of two images)
    10)Compute the negative of an image
    11)Can extract text from the image

    Technology Used: Python
--------------------------------------------------------------
"""

# Code for IP software starts here:

# importing necessary packages
from PIL import Image, ImageOps
import cv2
import numpy as np

# inputing file path
filename = "wanda.png"

# copying file path to different variables to perform different operations
img0 = Image.open(filename)
img1 = Image.open(filename)
img2 = Image.open(filename)
img3 = Image.open(filename)
img4 = Image.open(filename)
img5 = Image.open(filename)
img6 = Image.open(filename)

# rotating at certain angle
rotation_angle = input("Input angle of rotation: ")
rotation_angle = int(rotation_angle)
img = img0.rotate(angle=rotation_angle,expand=True,fillcolor="green")
img0.show()

# resizing at some width & height
resize_width = input("Input width (in %): ")
resize_width = float(resize_width)
resize_height = input("Input height (in %): ")
resize_height = float(resize_height)
img1 = img1.resize((int(img1.width*resize_width),int(img1.height*resize_height)))
img1.show()

# croping using intial coordinates & length of sides of image
startingX = input("Input initial X-coordinate: ")
startingX = int(startingX)
startingY = input("Input initial Y-coordinate: ")
startingY = int(startingY)
Width = input("Input width of croped image")
Width = int(Width)
Height = input("Input height of croped image: ")
Height = int(Height)
img2 = img2.crop(box=(startingX, startingY, Width, Height))
img2.show()

# horizontal flipping
img3 = ImageOps.mirror(img3)
img3.show()

# vertical flipping
img4 = ImageOps.flip(img4)
img4.show()

# reading pixels & applying negative transformation
for i in range(0, img5.size[0] - 1):
    for j in range(0, img5.size[1] - 1):
        # geting pixel value at (x,y) position of the image
        pixelColorVals = img5.getpixel((i, j));

        # inverting color
        redPixel = 255 - pixelColorVals[0];     # negate red pixel

        greenPixel = 255 - pixelColorVals[1];   # negate green pixel

        bluePixel = 255 - pixelColorVals[2];    # negate blue pixel

        # modifying the image with the inverted pixel values
        img5.putpixel((i, j), (redPixel, greenPixel, bluePixel));

# displaying the negative image
img5.show();

# converting RGB image into Black And White (Grayscale)
img6 = img6.convert('1')
img6.show();

# morphing 2 images (adding)
img7 = cv2.imread('pinuhuhuuhhuh1.png')
img8 = cv2.imread('wanda1.png')
dst = cv2.addWeighted(img7, 0.5, img8, 0.7, 0)
img_arr = np.hstack((img7, img8))
cv2.imshow('Input Images',img_arr)
cv2.imshow('Blended Image',dst)

# end of program
cv2.waitKey(0)
cv2.destroyAllWindows()
