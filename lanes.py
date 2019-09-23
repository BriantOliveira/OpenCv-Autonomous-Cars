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

Step 1 - Convert Image to Grayscale
Step 2 - Reduce Noise (Gaussian Filter)
"""

image = cv2.imread('./Image/test_image.jpg')
lane_image = np.copy(image)

# Converting image with the rbg
# cv2.imshow('result', image)

# Converting the image to gray
gray = cv2.cvtColor(lane_image, cv2.COLOR_BGR2GRAY)

"""
Averaging out the pixels in the image to reduce noise will be done with the kernel.
Essentially this kernel of normally distributed numbers is run across our entire image 
and sets each pixel about equal to the weighted average of its neighboring pixels thus 
smoothing our image. We're not going to go over kernel convolution and how it does it 
just know that when we write this line of code inside of our editor blur is equal to C-v 
to dog Gosden blur what we're doing is applying a gaussian blur on a greyscale image with 
a 5 by 5 kernel the size of the kernel is dependent on specific situations a 5 by 5 kernel 
is a good size for most cases. But ultimately what that will do is returning a new image that 
we simply called blur. Applying the gaussian blur by involving our image with a kernel of Gaussian 
values reduces noise in our image back to our project set. Blur is equal to C-v to the gaussian blur.
"""
blur = cv2.GaussianBlur(gray, (5, 5), 0)

"""
A small derivative is a small change in intensity whereas a big 
derivative is a big change by computing the derivative in all directions 
of the image. We're computing the gradients. Since recall the gradient 
is the change in brightness over a series of pixels. So when we call 
the kidney function it does all of that for us. It computes the gradient 
in all directions of our blurred image CH and is then going to trace 
our strongest gradients as a series of white pixels. But notice these 
two arguments low threshold and high threshold. While this actually 
allows us to isolate the adjacent pixels that follow the strongest 
gradients if the gradient is larger than the upper threshold then it 
is accepted as an edge pixel. If it is below the lower threshold it is
rejected. If the gradient is between the thresholds then it will be 
accepted only if it is connected to a strong edge. The documentation 
itself recommends to use a ratio of 1 to 2 or 1 to 3 as such will 
use a low high threshold ratio of 1 to 3 50 to 150.
"""

canny = cv2.Canny(blur, 50, 150)

# Display image until you press any key of the keyboard 
cv2.imshow('result', canny)
cv2.waitKey(0)


