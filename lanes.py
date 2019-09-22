import cv2
import numpy as np 

"""
Edge Detection - Identifying sharp changes in intensity in adjacent pixels.

The canny edge detection technique
The goal of edge detection is to identify the boundaries of objects within images.
In essence we'll be using a detection to try and find regions in an image where there is a sharp change in 
intensity a sharp change in color before diving into this.
It's important to recognize that an image can mirror it as a matrix an array of pixels a pixel contains
the light intensity at some location in the image.Each pixels intensity denoted by a numeric value that ranges 
from 0 to 255 and intensity value of zero indicates no intensity.
[0 0 255 255]
[0 0 255 255]
[0 0 255 255]
[0 0 255 255]

If something is completely black Where s 255 represents maximum intensity something being completely
What's that being said gradient is that the change in brightness over a series of pixels.
A strong gradient indicates a steep change whereas a small gradient represents a shallow change on the 
right hand side and you're looking at the gradient of the soccerball the outline of white pixels corresponds 
to the discontinuity in brightness at the points the strengthen gradient.
This helps us identify edges in our image since an edge is defined by the difference in intensity values in 
adjacent pixels.And wherever there is a sharp change in intensity a rapid change in brightness wherever there 
is a strong gradient there is a corresponding bright pixel in the gradient image by tracing out all of these 
pixels we obtain the edges.
We're going to use this intuition to detect the edges in our road image.This is a multi-step process.
Step one being to convert our image to grayscale. Why convert it to grayscale. 
Well as we discussed earlier images are made up of pixels. A three channel color image would have red green 
and blue channels each pixel a combination of three intensity values whereas a greyscale image only has one 
channel each pixel with only one intensity value ranging from 0 to 255.

The point being by using a grayscale image processing a single channel is faster than processing a three channel 
color image and less computational intensive. Let's start implementing this inside of them. We've already loaded and 
read our image into an array. Now what we'll do is import numb pie as the alias and P We're going to work with a copy 
of this array by setting a link image is equal to pie dog copy image.
Thus copying our array into a new variable it's imperative that you actually make a copy of the array instead of just 
setting lane image is equal to image. If we do this any changes we make to Lane image will also be reflected in the 
original viewable array.
Always ensure that you make a copy whenever working with a race instead of just setting them equal directly. 
So what we'll do now is we'll create a grayscale from the color image. We'll do that by setting a variable. 
Gray is equal to see to and from our open CV library will call the function CVT color which converts an image from 
one color space to another. We'll be converting lane image. And the second argument for an R G B to grayscale conversion. 
We can use the flag C-v to dot color underscore R G B to gray. Very intuitive.And now instead of showing the color 
image will show the gray image. If we go to our terminal Python Layne's that p y everything works out accordingly. 
This was step number one. Step number two of edge detection will be two.
"""

image = cv2.imread('./Image/test_image.jpg')
lane_image = np.copy(image)

# Converting the image to gray
gray = cv2.cvtColor(lane_image, cv2.COLOR_BGR2GRAY)

# Converting image with the rbg
# cv2.imshow('result', image)

# Display image until you press any key of the keyboard 
cv2.imshow('result', gray)
cv2.waitKey(0)


