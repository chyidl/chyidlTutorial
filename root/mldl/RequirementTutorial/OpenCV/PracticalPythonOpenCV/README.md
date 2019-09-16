Welcome to OpenCV-Python Tutorials
==================================
> Computer vision is to understand the story unfolding in a picture. As huamns, this is quite simple. But for computers, the task is extremely difficult. we need methods to an-alyze, categorize, and quantify the contents of these images.

Introduction to OpenCV
----------------------
* OpenCV
> OpenCV was started at Intel in 1999 by _Gary Bradsky_ and the first release came out in 2000. _Vadim Pisarevsky_ joined _Gary Bradsky_ to manage Intel's Russian software OpenCV team.
> Currently OpenCV supports a wide variety of programming languages like C++, Python, Java etc and is available on different platforms including Windows, Linux, OS X, Android, iOS etc. Also, interfaces based on CUDA and OpenCL are also under active development for high-speed GPU operations.
> OpenCV-Python, it is a Python wrapper around original C++ implementation.

Gui Features in OpenCV
----------------------
* Getting Started with Images 
    - Warning: Color image loaded by OpenCV is in BGR mode, But Matplotlib displays in RGB mode. So color images will not be displyed correctly in Matplotlib if image is read with OpenCV

* Getting Started with Videos
    - 

Requirements
------------
* NumPy is a library for the Python programming language that (among other things) provides supports for large, multi-dimensional arrays.
* SciPy is Scientific Computing Tools for Python.
* matplotlib is a Python 2D plotting library which produces publication quality firgures in a variety of hardcopy formats and interactive across platforms.
* OpenCV is real-time image processing, The library itself is written in C/C++, but Python binding are provided when running the installer.
* Mahotas, just like OpenCV, relies on Numpy arrays. is a computer vision and image precessing library for Python.Much of the functionality implemented in Mahotas can be found in OpenCV, but in some cases, the Mahotas interface is just easier to use.
* Scikit-Learn is Machine Learning in Python. Scikit-learn also includes a handful of image feature extraction functions as well.
* Scikit-image : New algorithms right from academic papers can be found in scikit-image, but in order to (effectively) use these algorithms, you need to have developed some rigor and understanding in the computer vision field.

Contents
--------
> Create "conventience" methods to do common tasks like translation, rotation, and resizing.
- [imutils.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPythonOpenCV/imutils.py)

* Loading, Displaying, and Saving
> Load an image off disk, display it on screen, write it to file in a different format.
    - The Numpy shape (height, width, channels)
- [load_display_save.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPythonOpenCV/load_display_save_image.py)

* Image Basics
> how to access and manipulate pixels in OpenCV.
    - Most pixels are represented in two ways: 
        * grayscale In a grayscale image, each pixel has a value between 0 and 255, where zero corresponds to "black" and 255 cor-responds to "white".
        * color pixels are normally represented in the RGB color space. Each of the three colors is represented by an integer in the range 0 to 255, which indicates how "much" of the color there is. use an 8-bit unsigned integer to represent each color intensity.
    - Overview of the coordinate system
        * point(0, 0) corresponds to the upper left corner of the image.
- [getting_and_setting.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPythonOpenCV/getting_and_setting.py)

* DRAWING
    - OpenCV provides convenient, easy-to-use methods to draw shapes on an image
        * cv2.line 
        * cv2.rectangle 
        * cv2.circle 
- [drawing.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPythonOpenCV/drawing.py)

* IMAGE PROCESSING
    - basic image transformation: [translation, rotation, resizing, flipping, cropping, bitwisc, masking]
    - IMAGE TRANSFORMATIONS
- [translation.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPythonOpenCV/translation.py)
- [rotate.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPythonOpenCV/rotate.py)
- [resize.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPythonOpenCV/resize.py)
- [flipping.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPythonOpenCV/flipping.py)
- [crop.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPythonOpenCV/crop.py)
    - Numpy will perform modulo arithmetic and "wrap around"
    - OpenCV will perform clipping and ensure pixel values never fall outside the range [0, 255]
- [arithmetic.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPythonOpenCV/arithmetic.py)
- [bitwise.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/bitwise.py)
- [masking.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/masking.py)
- [splitting_and_merging.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/splitting_and_merging.py)
    - Hue-Saturation-Value (HSV) color space is more similar to how humans think and conceive of color.
- [colorspaces.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/colorspaces.py)

* HISTOGRAMS
> A histogram represents the distribution of pixel intensities
    - the histogram of an image, get a general understanding regarding the contrast, brightness, and intensity distribution.
- [grayscale_histogram.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/grayscale_histogram.py)
- [color_histograms.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/color_histograms.py)
- [equalize.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/equalize.py)
- [histogram_with_mask.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/histogram_with_mask.py)

* SMOOTHING AND BLURRING 
    - image processing and computer vision functions, such as thresholding and edge detection, perform better if the image is first smoothed or blurred.
    - the intention of our blurring methods has been to reduce noise and detail in an image.
- [blurring.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/blurring.py)

* THRESHOLDING 
    - Thresholding is the binarization of an image.
- [simple_thresholding.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/simple_thresholding.py)
- [adaptive_thresholding.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/adaptive_thresholding.py)
- [otsu_and_riddler.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/otsu_and_riddler.py)

* GRADIENTS AND EDGE DETECTION 
    - laplacian and sobel  
- [sobel_and_laplacian.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/sobel_and_laplacian.py)
    - canny edge detector 
        * blurring the image to remove noise 
        * computing Sobel gradient images in the x and y direction
- [canny.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/canny.py)

* CONTOURS
> A contour is a curve of points, with no gaps in the curve.
- [counting_coins.py](/root/mldl/RequirementTutorial/OpenCV/PracticalPython/counting_coins.py)
