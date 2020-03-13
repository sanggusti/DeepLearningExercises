OpenCV is an open-source library for various image processing and computer vision techniques that runs on a highly optimized C++ back-end, although it is available for use with Python and Java as well. It’s often helpful as part of your overall edge applications, whether using it’s built-in computer vision techniques or handling image processing.

Uses of OpenCV
There’s a lot of uses of OpenCV. In your case, you’ll largely focus on its ability to capture and read frames from video streams, as well as different pre-processing techniques, such as resizing an image to the expected input size of your model. It also has other pre-processing techniques like converting from one color space to another, which may help in extracting certain features from a frame. There are also plenty of computer vision techniques included, such as Canny Edge detection, which helps to extract edges from an image, and it extends even to a suite of different machine learning classifiers for tasks like face detection.

Useful OpenCV function
- VideoCapture - can read in a video or image and extract a frame from it for processing
- resize is used to resize a given frame
- cvtColor can convert between color spaces.
  - You may remember from awhile back that TensorFlow models are usually trained with RGB images, while OpenCV is going to load frames as BGR. There was a technique with the Model Optimizer that would build the TensorFlow model to appropriately handle BGR. If you did not add that additional argument at the time, you could use this function to convert each image to RGB, but that’s going to add a little extra processing time.
- rectangle - useful for drawing bounding boxes onto an output image
- imwrite - useful for saving down a given image

See the link further down below for more tutorials on OpenCV if you want to dive deeper

## Further Research
OpenCV has some [pretty extensive tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html) available if you want to dive deeper into this useful computer vision library. We'll look at some of the relevant material on handling camera and video inputs next.