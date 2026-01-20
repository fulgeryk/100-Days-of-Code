# NumPy's ndarray - Incredible Power at Your Fingertips!

import numpy as np
from numpy.random import random
import matplotlib.pyplot as plt
from PIL import Image #for reading image files

#1-Dimension
#Let’s create a 1-dimensional array (i.e., a “vector”)
my_array = np.array([1.1, 9.2, 8.1, 4.7])
#Show rows and columns
print(my_array.shape)
#We access an element in a ndarray similar to how we work with a Python List, namely by that element's index:
#Accessing elements by index
print(my_array[2])
#Let’s check the dimensions of my_array with the ndim attribute:
#Show dimensions of an array
print(my_array.ndim)

#2-Dimensions
#Note we have two pairs of square brackets. This array has 2 rows and 4 columns.
#NumPy refers to the dimensions as axes, so the first axis has length 2 and the second axis has length 4.
array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])

print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)

#Access the 3rd value in the 2nd row
print(array_2d[1,2])
#Acess all the values in first row
print(array_2d[0,:])

#N-Dimensions
#An array of 3 dimensions (or higher) is often referred to as a ”tensor”.
#Yes, that’s also where Tensorflow, the popular machine learning tool, gets its name. A tensor simply refers to an n-dimensional array.
# Using what you've learned about 1- and 2-dimensional arrays, can you apply the same techniques to tackle a more complex array?

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                          [[7, 86, 6, 98],
                           [5, 1, 0, 4]],
                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

print(f'mystery_array has {mystery_array.ndim} dimensions')
print(f'Its shape is {mystery_array.shape}')
#Try to access the value 18 in the last line of code.
#Axis 0: 3rd element. Axis1:2nd element. Axis 3: 4th element
print(mystery_array[2,1,3])
#Try to retrieve a 1-dimensional vector with the values [97, 0, 27, 18]
#Retrieve all the elements on the 3rd axis that are at
#position 2 on the first axis and position 1 on the second axis
print(mystery_array[2,1,:])
#Try to retrieve a (3,2) matrix with the values [[ 0, 4], [ 7, 5], [ 5, 97]]
#All the first element on axis number 3
print(mystery_array[:,:,0])

#Generating and Manipulating ndarrays

#Challenge 1
#Use .arange()to createa a vector a with values ranging from 10 to 29. You should get this:
a = np.arange(10, 30, 1)
print(a)

#Challenge 2
#Create an array containing only the last 3 values of a
last_three_values_of_a = a[-3:]
print(last_three_values_of_a)
#Create a subset with only the 4th, 5th, and 6th values
subset_only_with = a[3:6]
print(subset_only_with)
#Create a subset of a containing all the values except for the first 12 (i.e., [22, 23, 24, 25, 26, 27, 28, 29])
all_the_value_expect_first_twelve = a[12:]
print(all_the_value_expect_first_twelve)
#Create a subset that only contains the even numbers (i.e, every second number)
even_numbers = a[::2]
print(even_numbers)

#Challenge 3
#Reverse the order of the values in a, so that the first element comes last:
flip_array = np.flip(a)
print(flip_array)

#Challenge 4
#Print out all the indices of the non-zero elements in this array: [6,0,9,0,0,5,0]
new_array = np.array([6,0,9,0,0,5,0])
list_without_zero= np.nonzero(new_array)
print(list_without_zero)

#Challenge 5
#Use NumPy to generate a 3x3x3 array with random numbers
rng = random((3,3,3))
print(rng.shape)

#Challenge 6
#Use .linspace() to create a vector x of size 9 with values spaced out evenly between 0 to 100 (both included).
x = np.linspace(0,100, num=9)
print(x)

#Challenge 7
#Use .linspace() to create another vector y of size 9 with values between -3 to 3 (both included). Then plot x and y on a line chart using Matplotlib.
y = np.linspace(-3, 3, num=9)
print(y)

plt.figure(figsize=(14,8), dpi=120)
plt.plot(x,y)


#Challenge 8
#Use NumPy to generate an array called noise with shape 128x128x3 that has random values. Then use Matplotlib's .imshow() to display the array as an image.
noise = random((128,128,3))
print(noise.shape)
plt.imshow(noise)
# plt.show()

#Broadcasting, Scalars and Matrix Multiplication

#Linear Algebra with Vectors

v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])

add_them = v1 + v2
print(add_them)

#In contrast, if we had two Python Lists

list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]

#adding them together would just concatenate the lists.

new_list = list1 + list2
print(new_list)

#Broadcasting
#Now, oftentimes you'll want to do some sort of operation between an array and a single number. In mathematics, this single number is often called a scalar.
# For example, you might want to multiply every value in your NumPy array by 2:

array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8]])
array_2d = array_2d + 10
print(array_2d)

array_2d = array_2d * 5
print(array_2d)

#Matrix Multiplication
#But what if we're not multiplying our ndarray by a single number?
# What if we multiply it by another vector or a 2-dimensional array? In this case, we follow the rules of linear algebra.

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

#Challenge: Let's multiply a1 with b1. Looking at the Wikipedia example above, work out the values for c12 and c33 on paper.
# Then use the .matmul() function or the @ operator to check your work.

c = np.matmul(a1,b1)
print(f"Matrix c has {c.shape[0]} rows and {c.shape[1]} columns.")
print(c)

print(a1 @ b1)

#Manipulating Images as ndarrays
#Images are nothing other than a collection of pixels. And each pixel is nothing other than value for a colour.
#And any colour can be represented as a combination of red, green, and blue (RGB).
img = np.array(Image.open("yummy_macarons.jpg"))

#Challenge
#What is the data type of img? Also, what is the shape of img and how many dimensions does it have? What is the resolution of the image?
print(type(img))
print(img.shape)
print(img.ndim)
#Challenge
#Now can you try and convert the image to black and white? All you need need to do is use a formula.
#The first step is a division by a scalar
#Here NumPy will use broadcasting to divide all the values in our ndarray by 255.
sRGB_array = img / 255
#Next, we use matrix multiplication to multiply our two ndarrays together.
grey_vals = np.array([0.2126, 0.7152, 0.0722])
#These are the values given by the formula above
#We can either multiply them together with the @ operator or the .matmul() function.
img_gray = sRGB_array @ grey_vals
#The cmap parameter is important here. If we leave it out the function will not know that is dealing with a black and white image.

plt.imshow(img_gray, cmap='gray')
# plt.show()

#Challenge
#Can you manipulate the images by doing some operations on the underlying ndarrays? See if you can change the values in the ndarray so that:
# 1) You flip the grayscale image upside down like so:
flip_img = np.flip(img_gray)
plt.imshow(flip_img, cmap='gray')
# plt.show()

#2) Rotate the colour image:
plt.imshow(np.rot90(img))
# plt.show()

#3) Inverting colors:
plt.imshow(255 - img)
plt.show()
