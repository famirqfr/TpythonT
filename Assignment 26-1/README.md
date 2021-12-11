Q1
added a new way for blur
Median Blurring
Here, the function cv.medianBlur() takes the median of all the pixels under the kernel area and the central element is replaced with this median value. This is highly effective against salt-and-pepper noise in an image. Interestingly, in the above filters, the central element is a newly calculated value which may be a pixel value in the image or a new value. But in median blurring, the central element is always replaced by some pixel value in the image. It reduces the noise effectively. Its kernel size should be a positive odd integer.
In this demo, I added a 70% noise to our original image and applied median blurring. 
Check the result:

input:

![inputQ1](https://user-images.githubusercontent.com/61835401/145675159-82a9add3-6a48-43cd-849c-6372e503189a.jpg)

output:

![outputQ1](https://user-images.githubusercontent.com/61835401/145675157-16bbca58-9752-496d-bae2-89e2224c1803.jpg)  






Q2
in this assignment added line for Increase contrast and them check color in area.
Check the result:

https://user-images.githubusercontent.com/61835401/145675320-e806e328-9e49-4582-9454-db3a19eea863.mp4


Q3
Brightness and contrast adjustments
Two commonly used point processes are multiplication and addition with a constant:

g(x)=αf(x)+β
The parameters α>0 and β are often called the gain and bias parameters; sometimes these parameters are said to control contrast and brightness respectively.
You can think of f(x) as the source image pixels and g(x) as the output image pixels. Then, more conveniently we can write the expression as:

g(i,j)=α⋅f(i,j)+β
where i and j indicates that the pixel is located in the i-th row and j-th column.
Check the result:

Input:

![a](https://user-images.githubusercontent.com/61835401/145675381-02fbc2d6-559c-4a3e-95ca-4b7036a34f38.jpg)

Output:

![result](https://user-images.githubusercontent.com/61835401/145675497-2f93cb2e-065e-4119-a412-802869c186a4.jpg)


Q4
In this task, the first step increases the contrast and cuts the desktop play area, and finally detects the cells that contain that number and cuts
