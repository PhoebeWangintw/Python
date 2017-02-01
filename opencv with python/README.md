Here are some problems that I’ve encountered when I was installing openCV.
I hope the following Q&A can help you. :)

Q1: How to install openCV on macOS?
A1: Here’s the tutorial that I found on youtube.
https://www.youtube.com/watch?v=U49CVY8yOxw
By following the instructions, you can easily installed openCV on macOS.
As for openCV for C++ in Xcode, try this tutorial:
https://www.youtube.com/watch?v=XJeP1juuHHY
At first, I got compile error messages.
However, by deleting some linker flags that the error messages showed, it worked fine!

Q2: How to install openCV for python2?
A2: I found the solution on stackoverflow:
http://stackoverflow.com/questions/38787748/installing-opencv-3-1-with-anaconda-python3
In short, just type the command below in the terminal: (Don’t forget to install anaconda first!)
conda install -c https://conda.binstar.org/menpo opencv 

Q3: How to install openCV for python3?
A3: I found the solution by myself!
Type in the following command to install:
conda install -c menpo opencv3
Then you can try “import cv2” to see if it really works out or not.